n = int(input())
scores = list(map(int, input().split()))

total = 0
passed = 0
for score in scores:
	total += score
	if score >= 60:
		passed += 1

average = total / n
print(f"{average:.2f}")
print(passed)
