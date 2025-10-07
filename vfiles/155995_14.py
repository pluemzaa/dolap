key = int(input("Enter key: "))
text = "hello"
result = ""
code = (ord(ch) - ord('a') + key) % 26
result = chr(ord('a') + code)
print("Cipher of", text, "is", result)