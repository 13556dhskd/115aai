def parking_fee(minutes):
	"""計算個別停車費的函式"""
	if minutes == 0:
		return 0

	# 每 30 分鐘一個區間，不足 30 分鐘也算一個區間 (向上取整)
	intervals = (minutes + 29) // 30
	fee = intervals * 30

	# 單次停車費最高 200 元
	if fee > 200:
		fee = 200

	return fee


def main():
	# 讀取第一行：記錄數 N
	n = int(input())

	# 讀取第二行：N 個停車分鐘數
	minutes_list = list(map(int, input().split()))

	fees = []
	total_revenue = 0

	# 對每筆記錄呼叫 parking_fee 函式
	for m in minutes_list:
		f = parking_fee(m)
		fees.append(f)
		total_revenue += f

	# 第一行輸出 N 個費用，以一個空白分隔
	print(*fees)

	# 第二行輸出所有費用的總和
	print(total_revenue)


if __name__ == '__main__':
	main()
