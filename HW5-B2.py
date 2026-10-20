a, b, k = map(int, input().split())
count = 0
total = 0

for number in range(a, b + 1):
	if number % k == 0:
		count += 1
		total += number

print(count, total)
