text = input("Enter input: ")
ciphertext = ""
index = len(text) - 1
while index >= 0:
    ciphertext += text[index]
    index -= 1
print(ciphertext)