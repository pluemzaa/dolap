key = int(input("Enter key: "))
text = "hello"
cipher = ""
cipher += chr((ord(ch) - 97 + key) % 26 + 97)
print("Cipher of", text, "is", cipher)