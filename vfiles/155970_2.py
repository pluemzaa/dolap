text = "hello"
key = int(input("Enter key: "))

result = ""

for char in text:
    position = ord(char) - ord('a')
    new_position = (position + key) % 26
    new_char = chr(new_position + ord('a'))
    result += new_char
  
print("Cipher of", text, "is", result)