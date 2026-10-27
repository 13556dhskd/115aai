def main():
    # 1. 讀取菜單
    M = int(input())
    menu_names = []
    menu_prices = []
    menu_totals = []  # 記錄每種飲料的總杯數
    
    for _ in range(M):
        line = input().split()
        name = line[0]
        price = int(line[1])
        menu_names.append(name)
        menu_prices.append(price)
        menu_totals.append(0)
        
    # 2. 讀取訂單
    N = int(input())
    student_names = []
    # student_orders[i][j] 記錄第 i 個學生購買第 j 種飲料的數量
    student_orders = []
    
    for _ in range(N):
        line = input().split()
        s_name = line[0]
        d_name = line[1]
        qty = int(line[2])
        
        # 找出飲料在菜單中的索引
        d_idx = menu_names.index(d_name)
        # 累加該飲料總杯數
        menu_totals[d_idx] += qty
        
        # 檢查學生是否已經存在於 student_names 中
        if s_name not in student_names:
            student_names.append(s_name)
            student_orders.append([0] * M)
            
        s_idx = student_names.index(s_name)
        student_orders[s_idx][d_idx] += qty

    # 3. 計算折扣後單價：總杯數達 10 杯（含）時，所有杯數單價皆減 5 元
    final_prices = []
    for i in range(M):
        if menu_totals[i] >= 10:
            final_prices.append(menu_prices[i] - 5)
        else:
            final_prices.append(menu_prices[i])

    # 4. 輸出第一部分：每種飲料總杯數（依菜單順序）
    for i in range(M):
        print(f"DRINK {menu_names[i]} {menu_totals[i]}")

    # 5. 計算並輸出第二部分：每個學生應付金額（依首次出現順序），並統計全班總金額
    total_revenue = 0
    for i in range(len(student_names)):
        s_bill = 0
        for j in range(M):
            s_bill += student_orders[i][j] * final_prices[j]
        total_revenue += s_bill
        print(f"STUDENT {student_names[i]} {s_bill}")

    # 6. 輸出最後總金額
    print(f"TOTAL {total_revenue}")

if __name__ == "__main__":
    main()