import sys

def main():
    # 使用 sys.stdin.read().splitlines() 完整讀取輸入，確保保留頭尾與連續空白
    input_data = sys.stdin.read().splitlines()
    if not input_data:
        return
    
    K = int(input_data[0].strip())
    # 取得第二行的原始訊息
    S = input_data[1] if len(input_data) > 1 else ""
    
    encrypted_chars = []
    
    for char in S:
        if 'A' <= char <= 'Z':
            # 大寫字母向後移動 K 個位置，超過 Z 則循環
            new_char = chr((ord(char) - ord('A') + K) % 26 + ord('A'))
            encrypted_chars.append(new_char)
        elif 'a' <= char <= 'z':
            # 小寫字母向後移動 K 個位置，超過 z 則循環
            new_char = chr((ord(char) - ord('a') + K) % 26 + ord('a'))
            encrypted_chars.append(new_char)
        else:
            # 非英文字母（數字、空白、標點符號）保持原樣
            encrypted_chars.append(char)
            
    # 將結果組合成字串並輸出
    print("".join(encrypted_chars))

if __name__ == "__main__":
    main()