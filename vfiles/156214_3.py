key = int(input("Enter key"))
text = "hello"

a = ord(text[0]) - ord('a')
b = ord(text[1]) - ord('a')
c = ord(text[2]) - ord('a')
d = ord(text[3]) - ord('a')
e = ord(text[4]) - ord('a')

a = (a + key) % 26
b = (b + key) % 26
c = (c + key) % 26
d = (d + key) % 26
e = (e + key) % 26

ca = chr(a + ord('a'))
cb = chr(b + ord('a'))
cc = chr(c + ord('a'))
cd = chr(d + ord('a'))
ce = chr(e + ord('a'))

cipher = ca + cb + cc + cd + ce

print("Cipher of hello is", cipher)