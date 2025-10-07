key = int(input("Enter key"))
text = "hello"
result = ""
for char in text:
    new_char = chr((ord(char) - ord('a') + key) % 26 + ord('a'))
    result += new_char