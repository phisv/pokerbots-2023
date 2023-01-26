import eval7

NUMS = [str(i) for i in range(2, 10)] + ['T','J','Q','K','A']
SUITS = ['c','d','h','s']
CARDS = [num + suit for num in NUMS for suit in SUITS]

def cur_val(cards):
	return eval7.evaluate([eval7.Card(c) for c in cards])

def analyze(cards):
	cur = cur_val(cards)
	out = outs(cards)
	return cur, out
def outs(cards):
	good = 0
	valid = 0
	current = cur_val(hand) // 1000000
	for card in CARDS:
		if card not in cards:
			valid += 1
			temp = cur_val(card + cards) // 1000000
			if temp > current:
				good += 1
	return good

