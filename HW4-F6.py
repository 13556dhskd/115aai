# 讀取三邊長
nums = list(map(int, input().split()))
a, b, c = nums

# 判斷是否能形成三角形
if a + b <= c or a + c <= b or b + c <= a:
    print("Invalid")
else:
    # 依邊長分類
    if a == b == c:
        print("Equilateral")
    elif a == b or b == c or a == c:
        print("Isosceles")
    else:
        print("Scalene")

