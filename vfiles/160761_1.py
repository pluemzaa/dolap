text = input("Enter input: ")
reverse_cipher= ""
for char in text:
    reverse_cipher = char + reverse_cipher
print(reverse_cipher)