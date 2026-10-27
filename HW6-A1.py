import sys

B, N, R, C = map(int, sys.stdin.readline().split())
T = max(0, B + B * R // 100 - C)
q, b = divmod(T, N)
a = N - b

print(T)
print(q, a)
print(q + 1, b)
