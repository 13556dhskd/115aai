s, d, t = map(int, input().split())

days = 0
while s < t:
	s += d
	days += 1

print(days)
