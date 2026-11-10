def gcd(a, b):
    """使用遞迴與輾轉相除法計算最大公因數"""
    if b == 0:
        return a
    return gcd(b, a % b)

def simplify_recipe(tea, milk, syrup):
    """計算三數的最大公因數並回傳最簡比例值"""
    # 先找出三個數中的最大公因數
    # 注意：某些材料可能為 0，但題目保證不會三項都為 0
    common_divisor = gcd(tea, gcd(milk, syrup))
    
    # 將三項用量除以最大公因數得到最簡整數比例
    return tea // common_divisor, milk // common_divisor, syrup // common_divisor

def main():
    # 讀取第一行：配方數 N
    n = int(input())
    
    # 依序讀取 N 行配方
    for _ in range(n):
        tea, milk, syrup = map(int, input().split())
        
        # 呼叫 simplify_recipe 取得化簡後的比例
        t, m, s = simplify_recipe(tea, milk, syrup)
        
        # 輸出三個以空白分隔的整數
        print(f"{t} {m} {s}")

if __name__ == '__main__':
    main()