key = int(input("Enter key"))
text = "hello"
result = ""
for char in text:
  ascii_code = ord(char)
  new_code =(ascii_code - 97 + key) % 26 + 97
  result += chr(new_code)
  print(f"Cipher of {text} is {result}")