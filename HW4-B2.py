y = int(input().strip())

if y % 400 == 0:
    print("Leap")
elif y % 100 == 0:
    print("Common")
elif y % 4 == 0:
    print("Leap")
else:
    print("Common")
