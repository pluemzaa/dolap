key = int(input("Enter key"))
text = "hello"
cipher = ""

for อุอิอ้า in text:
    num = ord(อุอิอ้า) - ord('a')
    num = ( num + key ) % 26
    cipher += chr(num  + ord('a'))

print("Cipher of hello is", cipher)