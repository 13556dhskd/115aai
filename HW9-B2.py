# 讀取一個整數代表西元年份 YYYY
year = int(input())

# 判斷閏年條件：
# 1. 能被 4 整除 (year % 4 == 0) 且 不能被 100 整除 (year % 100 != 0)
# 2. 或者 能被 400 整除 (year % 400 == 0)
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    # 注意 f-string 中冒號前後都有半形空格
    print(f"{year} : Leap Year")
else:
    print(f"{year} : Not a Leap Year")