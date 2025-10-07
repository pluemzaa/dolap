key = int(input("Enter key"))
text = "hello"

h = chr((ord(text[0]) - ord('a') + key) % 26 + ord('a'))
e = chr((ord(text[1]) - ord('a') + key) % 26 + ord('a'))
l1 = chr((ord(text[2]) - ord('a') + key) % 26 + ord('a'))
l2 = chr((ord(text[3]) - ord('a') + key) % 26 + ord('a'))
o = chr((ord(text[4]) - ord('a') + key) % 26 + ord('a'))

cipher = h + e + l1 + l2 + o

print("Cipher of hello is", cipher)