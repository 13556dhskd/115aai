# 讀取紀錄數 N
n = int(input())

# 使用 set 來儲存不重複的 (student, booth) tuple，過濾掉同一人在同一攤位的重複掃描
unique_records = set()

for _ in range(n):
    student, booth = input().split()
    unique_records.add((student, booth))

# 統計有效集章總數
total_valid_stamps = len(unique_records)

# 使用 dict 統計每位學生的不同攤位章數 (student -> count)
student_counts = {}
for student, booth in unique_records:
    if student in student_counts:
        student_counts[student] += 1
    else:
        student_counts[student] = 1

# 將 dict 轉換為 list 儲存並進行多重條件排序
# 排序規則：
# 1. 章數多者在前 (使用 -item[1] 實現降冪排序)
# 2. 姓名字典序較小者在前 (使用 item[0] 實現升冪排序)
ranking_list = sorted(student_counts.items(), key=lambda item: (-item[1], item[0]))

# 輸出有效集章總數
print(total_valid_stamps)

# 輸出排行榜：每行輸出 姓名 章數
for student, count in ranking_list:
    print(f"{student} {count}")