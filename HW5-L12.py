amount = int(input())
coin_count = 0

while amount > 0:
	if amount >= 50:
		amount -= 50
	elif amount >= 10:
		amount -= 10
	elif amount >= 5:
		amount -= 5
	else:
		amount -= 1
	coin_count += 1

print(coin_count)
