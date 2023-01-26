import eval7
import numpy as np
import random
import hands
import cards
from skeleton.actions import FoldAction, CallAction, CheckAction, RaiseAction


# def eval_hand(cards):
# 	hand = eval7.evaluate([eval7.Card(s) for s in cards])
# 	if eval7.handtype(hand) == 'Pair':
# 		return True #always play pocket pairs
# 	elif hand > 55000:
# 		return random.random() > 0.2 #play 80% of the time
# 	else:
# 		return False
# 		# return random.random() > 0.9  #play 20% of the time

# def eval_with_board(my, board):
# 	hand = eval7.evaluate([eval7.Card(s) for s in my+board])
# 	if hand > 3500000:
# 		return True
# 	return random.random() > 0.8 #play 20% of time
def get_opp_action(legal_actions,my_pip,opp_pip,my_contribution,opp_contribution): #find opponent action
	print(my_pip,opp_pip,my_contribution,opp_contribution)
	opp = None
	raise_amt = 0

	if my_contribution == opp_contribution:
		pass
	else:
		raise_amt = opp_pip - my_pip
		opp = RaiseAction(raise_amt)
	# if my_contribution == opp_contribution and opp_pip == 0:
	# 	opp = CheckAction()
	# elif opp_pip == my_pip: #opponent called me
	# 	opp = CallAction()
	# else:
	# 	raise_amt = opp_pip - my_pip
	# 	opp = RaiseAction(raise_amt)

	return opp, raise_amt

def eval_preflop(mycards,mypip,opppip,big_blind):
	
	good = 5.4
	bad = 0
	# handeval = eval7.evaluate([eval7.Card(s) for s in mycards])
	handeval = hands.chen(mycards)
	print(mycards,handeval,mypip,opppip)
	if mypip == 1 and opppip == 2: #starting as small blind
		if handeval > good:
			return 6
		else:
			return CallAction()
	if mypip == 2: #start as big blind
		if opppip == 2:
			if handeval > good:
				return 6
			return CheckAction()
		elif handeval < bad:
			return FoldAction()
		elif opppip < 10:
			if handeval > good:
				return 20
			else:
				return CallAction()
		elif opppip >= 10:
			if handeval > good:
				return CallAction()
		return FoldAction()
	else: #action returns to you
		if opppip > 50:
			return FoldAction()
		else:
			return CallAction()

	return None

def eval_flop(mycards,board,mypip,opppip,legal_actions,pot_size):
	print(mycards,board,mypip,opppip,pot_size)
	handeval, outs = cards.analyze(mycards+board)
	good = 10_000_000
	bad = 7
	if handeval > good: #made hand, raise pot
		return pot_size
	elif outs < bad: #no draws
		if CheckAction() in legal_actions:
			return CheckAction()
		if opppip < pot_size/5: #small bet
			return CallAction()
		return FoldAction()
	else: #draw hand
		if outs >= 13:
			return pot_size*3/4
		else:
			if CheckAction() in legal_actions:
				return CheckAction()
			if opppip < pot_size/5: #small bet
				return CallAction()
			return FoldAction()


hand = eval7.evaluate([eval7.Card(s) for s in ('9s', 'Tc')])
# print(eval7.evaluate(hand))
# print(hand)
# print(hands.chen(['9s','Tc']))