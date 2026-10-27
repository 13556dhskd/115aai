account = input().strip().lower()
account = "_".join(account.split())

valid = 6 <= len(account) <= 16 and all(
	"a" <= char <= "z" or "0" <= char <= "9" or char == "_"
	for char in account
)

print(account)
print("VALID" if valid else "INVALID")
