a = int(input("Enter key"))
text = "hello"
result = ""
for char in text:
  ascii_code = ora(char)
  new_code =(ascii_code -97 + a)% 26+97
  result += chr(new_code)
  print(f"Cipher of {text} is {result}")