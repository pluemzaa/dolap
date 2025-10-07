key = int(input("Enter key"))
text = "hello"
result = ""

for ch in text:
    pos = ord(ch) - ord('a')
    new_pos = (pos + key) % 26
    new_char = chr(new_pos + ord('a'))
    result = result + new_char

print("Cipher of", text, "is", result)