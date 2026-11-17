# 讀取記錄數 N
n = int(input())

# 1. 使用 list 保存輸入記錄，每筆為 tuple (user, item)
raw_records = []
for _ in range(n):
    user, item = input().split()
    raw_records.append((user, item))

# 讀取最後一行的 target 與 K
target_line = input().split()
target_user = target_line[0]
k = int(target_line[1])

# 2. 使用 dict 將使用者對應到商品的 set (自動去重)
user_purchases = {}
for user, item in raw_records:
    if user not in user_purchases:
        user_purchases[user] = set()
    user_purchases[user].add(item)

# 若目標使用者不在記錄中，則沒有任何購買記錄可言，直接輸出 0
if target_user not in user_purchases:
    print(0)
else:
    target_items = user_purchases[target_user]
    
    # 3. 透過交集與差集判斷相似使用者與候選商品
    candidate_scores = {} # 用 dict 累計候選商品分數 (item -> score)
    
    for other_user, items in user_purchases.items():
        if other_user == target_user:
            continue
        
        # 透過交集判斷是否為相似使用者 (至少有一件相同商品)
        common_items = target_items & items
        if len(common_items) > 0:
            # 透過差集找出該相似使用者買過、但目標使用者未買過的商品 (候選商品)
            recommended_items = items - target_items
            
            # 4. 以 dict 累計分數：買過該商品的相似使用者人數
            for item in recommended_items:
                if item not in candidate_scores:
                    candidate_scores[item] = 0
                candidate_scores[item] += 1

    # 5. 將 dict 轉為 list 進行排序
    # 排序規則：分數由大到小 (-score)，同分依商品名稱字典序 (item)
    sorted_candidates = sorted(candidate_scores.items(), key=lambda x: (-x[1], x[0]))
    
    # 計算實際推薦數量 R = min(K, 候選數)
    r = min(k, len(sorted_candidates))
    
    # 輸出結果
    if r == 0:
        print(0)
    else:
        print(r)
        for item, score in sorted_candidates[:r]:
            print(f"{item} {score}")