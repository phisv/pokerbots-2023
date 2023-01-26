import eval7
import numpy as np
import random
import hands
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
def get_opp_action(legal_actions,my_pip,opp_pip,mypip_history,opppip_history): #find opponent action
	print(legal_actions,my_pip,opp_pip)
	opp = None
	if opp_pip == my_pip: #opponent called me
		opp = CallAction()
	return None
	#incomplete
	# print('opponent just played:', opp_action)

def eval_preflop(mycards,mypip,opppip):
	
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

def eval_flop(mycards,board,mypip,opppip):
	return None


hand = eval7.evaluate([eval7.Card(s) for s in ('9s', 'Tc')])
# print(eval7.evaluate(hand))
# print(hand)
# print(hands.chen(['9s','Tc']))