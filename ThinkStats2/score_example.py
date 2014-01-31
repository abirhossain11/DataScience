"""Ryan Louie - score_example.py
Excercise 3.2 from ThinkStats2 by Allen Downey
"""

def PercentileRank(scores, your_score):
	count = 0
	for score in scores:
		if score <= your_score:
			count += 1

	percentile_rank = 100.0 * count / len(scores)
	return percentile_rank

def Percentile(scores, percentile_rank):
	scores.sort()
	index = int(percentile_rank/100 * len(scores) - 1)
	return scores[index]


def main():

	scores = [55, 66, 77, 88, 99]

	percentile_rank = PercentileRank(scores, 88)
	print 'percentile_rank = ', percentile_rank

	percentile = Percentile(scores, percentile_rank)
	print 'percentile = ', percentile

if __name__ == '__main__':
	main()
