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
#y = input("กรอก : ข้อความ,key").split(',')
#x = y[0]
key = int(input())
#cipher_encrypt(str(x),int(key))
cipher_encrypt("hello",int(key))