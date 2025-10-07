key = int(input("Enter key"))
text = "hello"
cipher_text = ""
for ch in text:
  index = ord(ch)-ord('a')
  new_index = (index = key)%26
  new_char =
chr(new_index+ord('a'))
  cipher_text += new_char
print("cipher of",text, "is",cipher_text)