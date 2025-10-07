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

message_key = ['h', 'e', 'l', 'l', 'o']
message_0 = (letter_to_number[message_key[0]] + key) % 26
message_1 = (letter_to_number[message_key[1]] + key) % 26
message_2 = (letter_to_number[message_key[2]] + key) % 26
message_3 = (letter_to_number[message_key[3]] + key) % 26
message_4 = (letter_to_number[message_key[4]] + key) % 26

cipher_text = Caesar_cipher[message_0] + Caesar_cipher[message_1] + Caesar_cipher[message_2] + Caesar_cipher[message_3] + Caesar_cipher[message_4]

print("Cipher of hello is", cipher_text)