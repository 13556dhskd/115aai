import sys


def count_ways(step, n, blocked, memo):
	"""使用遞迴與記憶化搜尋計算從目前位置 step 到達 n 的走法數"""
	# 基準情況 1：超過目標階梯，走法為 0
	if step > n:
		return 0

	# 基準情況 2：目前位置是損壞的階梯，不能停留在上面，走法為 0
	if blocked[step]:
		return 0

	# 基準情況 3：剛好到達第 n 階，算 1 種成功走法
	if step == n:
		return 1

	# 檢查 memo 是否已經計算過此位置的走法
	if memo[step] != -1:
		return memo[step]

	# 遞迴計算：分別嘗試跨出 1 階與跨出 2 階
	ways_1 = count_ways(step + 1, n, blocked, memo)
	ways_2 = count_ways(step + 2, n, blocked, memo)

	# 將結果存入 memo 陣列中以供後續重用
	memo[step] = ways_1 + ways_2

	return memo[step]


def main():
	# 讀取第一行：N 與 K
	input_data = sys.stdin.read().split()
	if not input_data:
		return

	n = int(input_data[0])
	k = int(input_data[1])

	# 建立長度 n + 1 的 blocked 串列，初值為 False
	blocked = [False] * (n + 1)

	# 若 K > 0，讀取 K 個損壞階梯編號
	if k > 0:
		for i in range(2, 2 + k):
			bad_step = int(input_data[i])
			blocked[bad_step] = True

	# 建立長度 n + 1 的 memo 串列，初值皆為 -1
	memo = [-1] * (n + 1)

	# 從地面 (0) 出發，呼叫 count_ways 函式
	result = count_ways(0, n, blocked, memo)

	# 輸出結果
	print(result)


if __name__ == '__main__':
	main()
