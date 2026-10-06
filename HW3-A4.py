import sys

x1, y1 = map(int, sys.stdin.readline().split())
x2, y2 = map(int, sys.stdin.readline().split())

dx = x2 - x1
dy = y2 - y1
print(dx * dx + dy * dy)

