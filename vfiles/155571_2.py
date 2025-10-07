def cipher_encrypt(s, key):
  encrypted_text = ""

  for i in s:
    shift_amout = key % 26
    if i.islower():
      start = ord('a')
      new_char = chr(start + (ord(i) - start + shift_amout) % 26)
    elif i.isupper():
      start = ord('A')
      new_char = chr(start + (ord(i) - start + shift_amout) % 26)
    encrypted_text += new_char
  print("Cipher of hello is",encrypted_text)
y = input()
y_split = y.split(',')
x = y_split[0]
key = y_split[1]
cipher_encrypt(str(x),int(key))