Caesar_cipher={0:'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h', 8: 'i', 9: 'j', 10: 'k', 11: 'l', 12: 'm', 13: 'n', 14: 'o', 15: 'p', 16: 'q', 17: 'r', 18: 's', 19: 't', 20: 'u', 21: 'v', 22: 'w', 23: 'x', 24: 'y', 25: 'z'}
key=int(input("Enter key"))
message_key = ['h','e','l','l','o']
message_key[0] = 7
message_key[0] = 4
message_key[0] = 12
message_key[0] = 12
message_key[0] = 14
message_0 = (message_key[0]+key)%26
message_1 = (message_key[1]+key)%26
message_2 = (message_key[2]+key)%26
message_3 = (message_key[3]+key)%26
message_4 = (message_key[4]+key)%26
print('Cipher of hello is',Caesar_cipher[message_0],Caesar_cipher[message_1],Caesar_cipher[message_2],Caesar_cipher[message_3],Caesar_cipher[message_4])