import sys


celsius = float(sys.stdin.readline().strip())
fahrenheit = 9 / 5 * celsius + 32
print(f"{fahrenheit:.1f}")
