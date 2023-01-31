import eval7
import numpy as np
import random
import hands
import cards
from skeleton.actions import FoldAction, CallAction, CheckAction, RaiseAction


def adjust_by_opp_sizes(oppaction_history,pot_history):
	print(oppaction_history)
	print(pot_history)
	
def get_opp_action(legal_actions,my_pip,opp_pip): #find opponent action
	print(my_pip,opp_pip)
	opp = None
	raise_amt = 0

	if my_pip == opp_pip:
		return CallAction()
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
		if mypip == 0:
			return pot_size
		return CallAction()
	elif outs < bad: #no draws
		if CheckAction() in legal_actions:
			return CheckAction()
		if opppip < pot_size/5: #small bet
			return CallAction()
		return FoldAction()
	else: #draw hand
		if outs >= 13:
			if mypip == 0:
				return pot_size*3//4
			return CallAction()
		else:
			if CheckAction() in legal_actions:
				return CheckAction()
			if opppip < pot_size/5: #small bet
				return CallAction()
			return FoldAction()
def eval_mid(mycards,board,mypip,opppip,legal_actions,pot_size):
	handeval, outs = cards.analyze(mycards+board)
	boardeval, bouts = cards.analyze(board)
	good = 20_000_000
	bad = 7
	if handeval > good and handeval > boardeval: #made hand, raise pot
		if mypip == 0:
			return pot_size
		return CallAction()
	elif outs < bad: #no draws
		if CheckAction() in legal_actions:
			return CheckAction()
		if opppip < pot_size/3: #small bet
			return CallAction()
		return FoldAction()
	else: #draw hand
		if outs >= 13 and outs > bouts:
			if mypip == 0:
				return pot_size*3//4
			return CallAction()
		else:
			if CheckAction() in legal_actions:
				return CheckAction()
			if opppip < pot_size/3: #small bet
				return CallAction()
			return FoldAction()

def eval_end(mycards,board,mypip,opppip,legal_actions,pot_size):
	handeval, outs = cards.analyze(mycards+board)
	boardeval, bouts = cards.analyze(board)
	good = 50_000_000
	if handeval > good and handeval > boardeval:
		if mypip == 0:
			return pot_size
		return CallAction()
	else:
		if CheckAction() in legal_actions:
			return CheckAction()
		if opppip < pot_size/3: #small bet
			return CallAction()
		return FoldAction()

hand = eval7.evaluate([eval7.Card(s) for s in ('9s', 'Tc')])
# print(eval7.evaluate(hand))
# print(hand)
# print(hands.chen(['9s','Tc']))