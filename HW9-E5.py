# 讀取正整數 N，同時保留原始輸入 original_N 供最後一行輸出使用
N = int(input())
original_N = N

# 記錄計算次數 (Pass)
pass_count = 0

# 使用 while True 搭配 break，確保即使一開始 N 就是個位數（如案例 3 的 5），也會執行至少一次 Pass 1
while True:
    pass_count += 1
    
    # 利用題目 HINT：將數字轉為字串 str(N)，逐一取出字元轉回 int() 並加總
    digit_sum = 0
    for ch in str(N):
        digit_sum += int(ch)
        
    # 依照格式輸出每次計算的暫時結果，注意冒號前後都有半形空格
    print(f"Pass {pass_count} : {digit_sum}")
    
    # 更新 N 為本次的各位數字之和
    N = digit_sum
    
    # 若結果已經是個位數（0~9，即 <= 9），則跳出迴圈
    if N <= 9:
        break

# 最後輸出原始數字與最終 Digital Root，同樣注意冒號前後的半形空格
print(f"Digital Root of {original_N} : {N}")