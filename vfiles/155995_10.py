alphabet = {i: chr(97 + i) for i in range(26)}
char_to_index = {v: k for k, v in alphabet.items()}
key = int(input("Enter key"))
text = "hello"
cipher = ""
print(f"Cipher of {text} is {cipher}")