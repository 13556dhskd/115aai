n = int(input())
reversed_number = 0

while n > 0:
	digit = n % 10
	reversed_number = reversed_number * 10 + digit
	n //= 10

print(reversed_number)
