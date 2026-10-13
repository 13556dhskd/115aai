h = int(input())
fee = min(h, 2) * 30 + min(max(h - 2, 0), 3) * 20 + max(h - 5, 0) * 10
print(fee)
