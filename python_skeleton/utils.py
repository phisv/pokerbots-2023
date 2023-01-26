import eval7
import numpy as np
import random


def eval_hand(cards):
	hand = eval7.evaluate([eval7.Card(s) for s in cards])
	if eval7.handtype(hand) == 'Pair':
		return True #always play pocket pairs
	elif hand > 55000:
		return random.random() > 0.2 #play 80% of the time
	else:
		return False
		# return random.random() > 0.9  #play 20% of the time

def eval_with_board(my, board):
	hand = eval7.evaluate([eval7.Card(s) for s in my+board])
	if hand > 3500000:
		return True
	return random.random() > 0.8 #play 20% of time

def eval_preflop(mycards,mypip,opppip):
	
	good = 590000
	bad = 400000
	handeval = eval7.evaluate([eval7.Card(s) for s in mycards])
	print(mycards,handeval,mypip,opppip)
	if mypip == 1 and opppip == 2: #starting as small blind
		if handeval > good:
			return 6
		else:
			return 'call'
	if mypip == 2: #start as big blind
		if opppip == 2:
			if handeval > good:
				return 6
			return 'check'
		elif handeval < bad:
			return 'fold'
		elif opppip < 10:
			if handeval > good:
				return 20
			else:
				return 'call'
		elif opppip >= 10:
			if handeval > good:
				return 'call'
		return 'fold'
	else: #action returns to you
		if opppip > 50:
			return 'fold'
		else:
			return 'call'

	return None


hand = eval7.evaluate([eval7.Card(s) for s in ('9s', 'Tc')])
# print(eval7.evaluate(hand))
# print(hand)
