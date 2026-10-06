# 讀取三個整數
nums = list(map(int, input().split()))

# 計算平均數與母體變異數
mean = sum(nums) / 3
variance = sum((x - mean) ** 2 for x in nums) / 3

# 輸出結果，保留兩位小數
print(f"{mean:.2f}")
print(f"{variance:.2f}")
