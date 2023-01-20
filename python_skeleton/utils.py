import eval7
import numpy as np
import random


def eval_hand(cards):
	hand = eval7.evaluate(cards)
	if eval7.handtype(hand) == 'Pair':
		return True #always play pocket pairs
	elif hand > 55000:
		return random.random() > 0.2 #play 80% of the time
	else:
		return False
		# return random.random() > 0.9  #play 20% of the time

def eval_with_board(my, board):
	hand = eval7.evaluate(my+board)
	if hand > 3500000:
		return True
	return random.random() > 0.8 #play 20% of time


hand = [eval7.Card(s) for s in ('9s', 'Tc')]
print(eval7.evaluate(hand))
