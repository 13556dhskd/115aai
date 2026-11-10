def is_prime(n):
    """判定是否為質數的函式，使用試除法檢查至平方根"""
    if n < 2:
        return False
    # 只需檢查至除數平方不大於 n 的範圍 (i * i <= n)
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

def main():
    # 讀取輸入的 L 與 R
    L, R = map(int, input().split())
    
    primes = []
    total_sum = 0
    
    # 對區間 [L, R] 內的每個整數呼叫 is_prime(n)
    for num in range(L, R + 1):
        if is_prime(num):
            primes.append(num)
            total_sum += num
            
    # 輸出第一行：若有質數則依遞增順序輸出，以空白分隔；若沒有則輸出 NONE
    if not primes:
        print("NONE")
        print("0 0")
    else:
        print(*(primes))
        print(f"{len(primes)} {total_sum}")

if __name__ == '__main__':
    main()