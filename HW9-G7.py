# 第一行：讀取由空白分隔的整數密鑰串列 keys，長度為 l
keys = list(map(int, input().split()))
l = len(keys)

# 第二行：讀取整行密文（可能包含空格與符號，因此使用 input() 整行讀取）
cipher = input()

result = []

# 走訪密文中的每一個字元，i 為字元在密文中的索引（從 0 開始）
for i, ch in enumerate(cipher):
    # 取得對應的密鑰位移量（當 i 超過 l 時，i % l 也能正確循環）
    shift = keys[i % l]
    # 解密方向與加密相反，因此位移量取負號
    dec_shift = -shift

    if 'A' <= ch <= 'Z':
        # 大寫字母在 'A'~'Z'（共 26 個字母）內循環
        # (ord(ch) - ord('A') + dec_shift) % 26 在 Python 中即使為負數也會正確落在 0~25
        idx = (ord(ch) - ord('A') + dec_shift) % 26
        result.append(chr(ord('A') + idx))
    elif 'a' <= ch <= 'z':
        # 小寫字母在 'a'~'z'（共 26 個字母）內各自獨立循環
        idx = (ord(ch) - ord('a') + dec_shift) % 26
        result.append(chr(ord('a') + idx))
    else:
        # 非英文字元（如空格、數字、符號）保持不變
        # 注意：索引 i 仍會隨著迴圈前進，與題目範例（如 'KFPOP ARSPG' -> 'HELLO WORLD'）一致
        result.append(ch)

# 單行輸出解密後的明文
print("".join(result))