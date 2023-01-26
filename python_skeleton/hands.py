import eval7
highs = {str(i):i / 2 for i in range(2, 11)} |  {'T':5,'J':6,'Q':7,'K':8,'A':10}
highs.pop('10')
nums = [str(i) for i in range(2, 10)] + ['T','J','Q','K','A']

def score(name):
	score = highs[name[0]]
	if name[0] == name[1]:
		score *= 2
		score = max(score, 5 + int(name[0] == '5'))
	if name[2] == 's':
		score += 2
	gap = nums.index(name[0]) - 1 - nums.index(name[1])
	if gap == 3:
		gap = 4
	elif gap > 3:
		gap = 5
	score -= gap
	if gap == 0 or (gap == 1 and nums.index(name[0]) < nums.index('Q')):
		score += 1
	return score

def chen(hand):
	vals = dict()
	for i, num1 in enumerate(nums):
		for num2 in nums[:i+1]:
			for suited, suit2 in {True:'h', False:'d'}.items():
				name = num1 + num2 + ('s' if suited else 'o')
				if suited and num1 == num2:
					continue
				vals[name] = score(name)
	suited = 's' if hand[0][1] == hand[1][1] else 'o'
	return max(vals.get(hand[0][0]+hand[1][0]+suited, -2), vals.get(hand[1][0]+hand[0][0]+suited, -2))

if __name__ == '__main__':
	pass
	# print(chen(['9s', 'Tc']))