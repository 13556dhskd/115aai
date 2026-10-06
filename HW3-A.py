N = int(input())

hundreds = N // 100
tens = (N // 10) % 10
ones = N % 10

print(hundreds, tens, ones)
print(hundreds + tens + ones)
print(hundreds * tens * ones)
print(ones * 100 + tens * 10 + hundreds)
