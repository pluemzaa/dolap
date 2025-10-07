k = int(input("Enter key"))
s = "hello"
print("Cipher of hello is", ''.join([chr((ord(c)-97+k)%26+97) for c in s]))