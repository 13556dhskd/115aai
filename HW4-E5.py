a, b, c = map(int, input().split())
discriminant = b * b - 4 * a * c

if discriminant > 0:
	print(2)
elif discriminant == 0:
	print(1)
else:
	print(0)
