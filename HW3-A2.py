seconds = int(input())
hours, remainder = divmod(seconds, 3600)
minutes, seconds = divmod(remainder, 60)
print(hours, minutes, seconds)
