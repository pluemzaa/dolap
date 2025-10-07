alphabet = {i: chr(97 + i) for i in range(26)}
reverse_alphabet = {v: k for k, v in alphabet.items()}
key_input = input("Enter key")
key = int(key_input)
text = "hello"
cipher_text = ""
for char in text:
    if char in reverse_alphabet:
        old_index = reverse_alphabet[char]
        new_index = (old_index + key) % 26
        cipher_text += alphabet[new_index]
    else:
        cipher_text += char  

print(f"Cipher of {text} is {text}")