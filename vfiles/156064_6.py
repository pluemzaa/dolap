Caesar_cipher = {
    0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h',
    8: 'i', 9: 'j', 10: 'k', 11: 'l', 12: 'm', 13: 'n', 14: 'o',
    15: 'p', 16: 'q', 17: 'r', 18: 's', 19: 't', 20: 'u', 21: 'v',
    22: 'w', 23: 'x', 24: 'y', 25: 'z'
}

letter_to_number = {
    'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7,
    'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14,
    'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21,
    'w': 22, 'x': 23, 'y': 24, 'z': 25
}

key = int(input("Enter key: "))

m0 = letter_to_number['h']
m1 = letter_to_number['e']
m2 = letter_to_number['l']
m3 = letter_to_number['l']
m4 = letter_to_number['o']

c0 = Caesar_cipher[(m0 + key) % 26]
c1 = Caesar_cipher[(m1 + key) % 26]
c2 = Caesar_cipher[(m2 + key) % 26]
c3 = Caesar_cipher[(m3 + key) % 26]
c4 = Caesar_cipher[(m4 + key) % 26]

cipher_text = c0 + c1 + c2 + c3 + c4

print("Cipher of hello is", cipher_text)