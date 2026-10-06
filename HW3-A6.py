import sys

a, b = map(int, sys.stdin.readline().split())
c, d = map(int, sys.stdin.readline().split())

det = a * d - b * c

print(f"{d / det:.4f} {-b / det:.4f}")
print(f"{-c / det:.4f} {a / det:.4f}")
