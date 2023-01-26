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

def pot(outs, num_cards):
	remaining = 2 + int(num_cards == 3)
	other = 52 - num_cards
	win_rate = 1 - (((other - outs) / other) ** remaining)
	return win_rate

def outs(cards):
	good = 0
	valid = 0
	current = cur_val(cards) // 10_000_000
	for card in CARDS:
		if card not in cards:
			valid += 1
			temp = cur_val([card] + cards) // 10_000_000
			if temp - 1 > current:
				good += 1 + int(card[1] in 'cs')
	return good

if __name__ == '__main__':
	print(analyze(['Ts','7c','2h','Ah','Ac']))