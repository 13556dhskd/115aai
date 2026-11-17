# 讀取初始商品數量 N
n = int(input())
inventory = {}

# 讀取初始商品與庫存，建立 dictionary
for _ in range(n):
    parts = input().split()
    item = parts[0]
    stock = int(parts[1])
    inventory[item] = stock

# 讀取指令數量 Q
q = int(input())

total_sold_qty = 0      # 成功售出總件數
rejected_buy_count = 0  # 被拒絕的購買筆數

# 依序處理 Q 個指令的迴圈
for _ in range(q):
    command = input().split()
    action = command[0]
    item = command[1]
    qty = int(command[2])
    
    if action == "ADD":
        # 若商品已存在則增加庫存，不存在則新增
        if item in inventory:
            inventory[item] += qty
        else:
            inventory[item] = qty
            
    elif action == "BUY":
        # 檢查商品是否存在且庫存是否充足
        if item in inventory and inventory[item] >= qty:
            inventory[item] -= qty
            total_sold_qty += qty
        else:
            rejected_buy_count += 1

# 輸出第一行：成功售出總件數與被拒絕的購買筆數
print(f"{total_sold_qty} {rejected_buy_count}")

# 輸出後續行：依商品名稱字典序輸出商品與最後庫存
for item in sorted(inventory.keys()):
    print(f"{item} {inventory[item]}")