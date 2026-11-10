import sys


def normalize(text):
	result = []
	for char in text:
		if "A" <= char <= "Z":
			result.append(chr(ord(char) + ord("a") - ord("A")))
		elif "a" <= char <= "z" or "0" <= char <= "9":
			result.append(char)
	return "".join(result)


def is_palindrome(text, left, right):
	if left >= right:
		return True
	if text[left] != text[right]:
		return False
	return is_palindrome(text, left + 1, right - 1)


text = normalize(sys.stdin.readline())
print("YES" if is_palindrome(text, 0, len(text) - 1) else "NO")
