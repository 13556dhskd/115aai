import sys


def best_total(prices, index, remaining):
	if index == len(prices):
		return 0

	best = best_total(prices, index + 1, remaining)
	if prices[index] <= remaining:
		best = max(
			best,
			prices[index]
			+ best_total(prices, index + 1, remaining - prices[index]),
		)
	return best


def main():
	data = list(map(int, sys.stdin.buffer.read().split()))
	if not data:
		return

	n, budget = data[0], data[1]
	prices = data[2 : 2 + n]
	print(best_total(prices, 0, budget))


if __name__ == "__main__":
	main()
