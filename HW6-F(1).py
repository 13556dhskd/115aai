import sys

def main():
    # 使用 sys.stdin.read().splitlines() 完整讀取輸入，避免頭尾或連續空白被 input() 忽略
    input_data = sys.stdin.read().splitlines()
    if not input_data:
        return
    
    K = int(input_data[0].strip())
    # 取得第二行的原始訊息（若第二行為空字串也需要能正確保留）
    S = input_data[1] if len(input_data) > 1 else ""
    
    encrypted_chars = []
    
    for char in S:
        if 'A' <= char <= 'Z':
            # 大寫字母加密
            new_char = chr((ord(char) - ord('A') + K) % 26 + ord('A'))
            encrypted_chars.append(new_char)
        elif 'a' <= char <= 'z':
            # 小寫字母加密
            new_char = chr((ord(char) - ord('a') + K) % 26 + ord('a'))
            encrypted_chars.append(new_char)
        else:
            # 非英文字母（數字、空白、標點符號）保持原樣
            encrypted_chars.append(char)
            
    # 將結果組合成字串並輸出
    print("".join(encrypted_chars))

if __name__ == "__main__":
    main()