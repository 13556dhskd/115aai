import sys

# 讀取矩陣 A 與 B
A = [list(map(int, sys.stdin.readline().split())) for _ in range(2)]
B = [list(map(int, sys.stdin.readline().split())) for _ in range(2)]

# 計算矩陣乘積 C = A × B
C = [[0, 0], [0, 0]]
for i in range(2):
    for j in range(2):
        C[i][j] = A[i][0] * B[0][j] + A[i][1] * B[1][j]

# 輸出結果
for row in C:
    print(*row)

