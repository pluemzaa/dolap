key_number = int(input("Enter key"))
text = "hello"
cipher_text = ""

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
           'n','o','p','q','r','s','t','u','v','w','x','y','z']

for letter in text:
    position = letters.index(letter)
    new_position = (position + key_number) % 26
    new_letter = letters[new_position]
    cipher_text = cipher_text + new_letter

print("Cipher of", text, "is", cipher_text)