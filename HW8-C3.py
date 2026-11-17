# 第一行：讀取 N 與 M（雖然在 Python 中直接 split() 即可處理空白行，但仍依規範讀取）
n, m = map(int, input().split())

# 第二行與第三行：讀取名單並直接轉換為 set 去除重複
# 當 N=0 或 M=0 時，該行為空白行，input().split() 會回傳空串列 []，set([]) 則為空集合 set()
set_a = set(input().split())
set_b = set(input().split())

# 進行四種集合運算，並依序存入串列中以便統一處理輸出
results = [
    set_a & set_b,  # 交集：共同成員
    set_a | set_b,  # 聯集：至少參加一個社團
    set_a - set_b,  # 差集 A - B：只參加 A 社團
    set_b - set_a   # 差集 B - A：只參加 B 社團
]

# 透過迴圈依序處理四行輸出
for res in results:
    if len(res) == 0:
        print("NONE")
    else:
        # 因為 set 無序，輸出前必須使用 sorted() 依字典序排列
        print(" ".join(sorted(res)))