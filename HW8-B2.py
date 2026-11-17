# 讀取跑者數 N
n = int(input())
runners = []

# 使用迴圈讀取每位跑者的資料並存入 tuple 收集到 list 中
for _ in range(n):
    parts = input().split()
    name = parts[0]
    time = int(parts[1])
    penalty = int(parts[2])
    runners.append((name, time, penalty))

# 依指定排序規則進行排序：
# 1. 總秒數 (time + penalty) 由小到大
# 2. 總秒數相同時，原始完賽秒數 (time) 較小在前
# 3. 兩者皆相同時，姓名字典序 (name) 較小在前
runners.sort(key=lambda x: (x[1] + x[2], x[1], x[0]))

# 輸出結果
for r in runners:
    total_time = r[1] + r[2]
    print(f"{r[0]} {total_time}")