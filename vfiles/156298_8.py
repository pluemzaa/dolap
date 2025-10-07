char_map = {i: chr(ord('a') + i) for i in range(26)}
reverse_map = {v: k for k, v in char_map.items()}

key = int(input(""))
plain_text = "hello"

def caesar_char(ch):
    return char_map[(reverse_map[ch] + key) % 26] if ch in reverse_map else ch

cipher_text = ''.join(map(caesar_char, plain_text))

print(f"Cipher of {plain_text} is {cipher_text}")