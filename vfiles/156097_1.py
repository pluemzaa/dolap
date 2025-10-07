def caesar_cipher(text, key):
    alphabet = {i: chr(97 + i) for i in range(26)}  # {0: 'a', 1: 'b', ..., 25: 'z'}
    result = ''

    for char in text:
        if char.isalpha():
            index = ord(char) - ord('a')
            new_index = (index + key) % 26
            result += alphabet[new_index]
        else:
            result += char  

    return result


key_input = input("Enter key")
try:
    key = int(key_input)
    text = "hello"
    cipher = caesar_cipher(text, key)
    print(f"Cipher of {text} is {cipher}")
except ValueError:
    print("Invalid key. Please enter an integer.")