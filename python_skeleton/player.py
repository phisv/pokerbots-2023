'''
Simple example pokerbot, written in Python.
'''
from skeleton.actions import FoldAction, CallAction, CheckAction, RaiseAction
from skeleton.states import GameState, TerminalState, RoundState
from skeleton.states import NUM_ROUNDS, STARTING_STACK, BIG_BLIND, SMALL_BLIND
from skeleton.bot import Bot
from skeleton.runner import parse_args, run_bot
import utils


class Player(Bot):
    '''
    A pokerbot.
    '''

    def __init__(self):
        '''
        Called when a new game starts. Called exactly once.

        Arguments:
        Nothing.

        Returns:
        Nothing.
        '''
        self.mypip_history = []
        self.opppip_history = []
        self.myaction_history = []
        self.oppaction_history = []

    def handle_new_round(self, game_state, round_state, active):
        '''
        Called when a new round starts. Called NUM_ROUNDS times.

        Arguments:
        game_state: the GameState object.
        round_state: the RoundState object.
        active: your player's index.

        Returns:
        Nothing.
        '''
        #my_bankroll = game_state.bankroll  # the total number of chips you've gained or lost from the beginning of the game to the start of this round
        #game_clock = game_state.game_clock  # the total number of seconds your bot has left to play this game
        #round_num = game_state.round_num  # the round number from 1 to NUM_ROUNDS
        #my_cards = round_state.hands[active]  # your cards
        # big_blind = bool(active)  # True if you are the big blind
        self.mypip_history = []
        self.opppip_history = []
        self.myaction_history = []
        self.oppaction_history = []

    def handle_round_over(self, game_state, terminal_state, active):
        '''
        Called when a round ends. Called NUM_ROUNDS times.

        Arguments:
        game_state: the GameState object.
        terminal_state: the TerminalState object.
        active: your player's index.

        Returns:
        Nothing.
        '''
        #my_delta = terminal_state.deltas[active]  # your bankroll change from this round
        #previous_state = terminal_state.previous_state  # RoundState before payoffs
        #street = previous_state.street  # int of street representing when this round ended
        #my_cards = previous_state.hands[active]  # your cards
        #opp_cards = previous_state.hands[1-active]  # opponent's cards or [] if not revealed
        pass

    def get_action(self, game_state, round_state, active):
        '''
        Where the magic happens - your code should implement this function.
        Called any time the engine needs an action from your bot.

        Arguments:
        game_state: the GameState object.
        round_state: the RoundState object.
        active: your player's index.

        Returns:
        Your action.
        '''
        legal_actions = round_state.legal_actions()  # the actions you are allowed to take
        street = round_state.street  # int representing pre-flop, flop, turn, or river respectively
        my_cards = round_state.hands[active]  # your cards
        board_cards = round_state.deck[:street]  # the board cards
        my_pip = round_state.pips[active]  # the number of chips you have contributed to the pot this round of betting
        opp_pip = round_state.pips[1-active]  # the number of chips your opponent has contributed to the pot this round of betting
        my_stack = round_state.stacks[active]  # the number of chips you have remaining
        opp_stack = round_state.stacks[1-active]  # the number of chips your opponent has remaining
        continue_cost = opp_pip - my_pip  # the number of chips needed to stay in the pot
        my_contribution = STARTING_STACK - my_stack  # the number of chips you have contributed to the pot
        opp_contribution = STARTING_STACK - opp_stack  # the number of chips your opponent has contributed to the pot
        pot_size = my_contribution+opp_contribution
        if RaiseAction in legal_actions:
           min_raise, max_raise = round_state.raise_bounds()  # the smallest and largest numbers of chips for a legal bet/raise
           min_cost = min_raise - my_pip  # the cost of a minimum bet/raise
           max_cost = max_raise - my_pip  # the cost of a maximum bet/raise
        big_blind = bool(active)

        opp_action = utils.get_opp_action(legal_actions,my_pip,opp_pip,my_contribution,opp_contribution)
        self.oppaction_history.append(opp_action)
        self.opppip_history.append(opp_pip)
        my_action = None
        print('opppip history',self.opppip_history)
        print('oppaction_history',self.oppaction_history)

        if street == 0:
            action = utils.eval_preflop(my_cards,my_pip,opp_pip,big_blind)
            if type(action) == int:
                return RaiseAction(action)
            return action

        elif street == 3: # flop
            print('flop')
            action = utils.eval_flop(my_cards,board_cards,my_pip,opp_pip,legal_actions,pot_size)
            if type(action) == int:
                if action < min_raise:
                    return RaiseAction(min_raise)
                return RaiseAction(action)
            return action
        elif street >= 5 and board_cards[-1][1] in ['c','s']: #last card
            print('ree',street)
            if CheckAction in legal_actions:
                return CheckAction()
            return CallAction()
        else: #turn/river/run
            print('asdf',street)
            if CheckAction in legal_actions:
                return CheckAction()
            return CallAction()

        

        


if __name__ == '__main__':
    run_bot(Player(), parse_args())
