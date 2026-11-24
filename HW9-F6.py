import math

# 讀取同一行以空白隔開的兩個正整數 A 和 B
A, B = map(int, input().split())

# 題目陷阱：A 與 B 大小關係不限（可能 A > B），但輸出必須「由小到大」
# 使用 min() 與 max() 自動將區間統一整理為 [start, end]
start = min(A, B)
end = max(A, B)

primes = []

# 走訪區間 [start, end]（包含端點，所以 end 要 + 1）
for num in range(start, end + 1):
    # 質數定義為「大於 1 的自然數」，因此 <= 1（例如案例 3 中的 1）直接跳過
    if num <= 1:
        continue
    
    # 假設 num 是質數，檢查從 2 到 sqrt(num) 是否有因數
    is_prime = True
    for i in range(2, int(math.isqrt(num)) + 1):
        if num % i == 0:
            is_prime = False
            break  # 只要找到一個因數就不是質數，提早跳出內層迴圈加速
            
    if is_prime:
        primes.append(str(num))

# 使用 " ".join() 將所有質數以單一空格隔開輸出
# 若區間內無質數（primes 為空串列），則會自動輸出一行空白，完全符合案例 2 要求
print(" ".join(primes))