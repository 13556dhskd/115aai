def main():
    N = int(input())
    
    names = []
    prices = []
    quantities = []
    subtotals = []
    
    for _ in range(N):
        line = input().split()
        name = line[0]
        price = int(line[1])
        qty = int(line[2])
        
        # 計算每種商品的優惠後小計：每買滿3件其中1件免費
        # 付費件數 = (qty // 3) * 2 + (qty % 3)
        paid_qty = (qty // 3) * 2 + (qty % 3)
        subtotal = paid_qty * price
        
        names.append(name)
        prices.append(price)
        quantities.append(qty)
        subtotals.append(subtotal)
        
    # 輸出第一部分：每種商品的名稱及優惠後小計
    for i in range(N):
        print(f"{names[i]} {subtotals[i]}")
        
    # 計算總和
    total_sum = sum(subtotals)
    
    # 合計滿 1000 元折 100 元，整張帳單限折一次
    if total_sum >= 1000:
        total_sum -= 100
        
    # 輸出第二部分：TOTAL 金額
    print(f"TOTAL {total_sum}")
    
    # 找出花費最多（小計最高）的商品，同額選輸入較早者
    max_subtotal = -1
    top_index = 0
    for i in range(N):
        if subtotals[i] > max_subtotal:
            max_subtotal = subtotals[i]
            top_index = i
            
    # 輸出第三部分：TOP 商品名稱
    print(f"TOP {names[top_index]}")

if __name__ == "__main__":
    main()