keys = list(map(int, input().split()))
key_len = len(keys)
cipher = input()

if key_len == 0:
    print(cipher)
else:
    result = []
    for i, ch in enumerate(cipher):
        dec_shift = -keys[i % key_len]

        if 'A' <= ch <= 'Z':
            idx = (ord(ch) - ord('A') + dec_shift) % 26
            result.append(chr(ord('A') + idx))
        elif 'a' <= ch <= 'z':
            idx = (ord(ch) - ord('a') + dec_shift) % 26
            result.append(chr(ord('a') + idx))
        else:
            result.append(ch)

    print("".join(result))