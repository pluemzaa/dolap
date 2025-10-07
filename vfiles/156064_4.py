Caesar_cipher = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n',
                 'o','p','q','r','s','t','u','v','w','x','y','z']

key = int(input("Enter key: "))

message_key = ['h','e','l','l','o']

message_key[0] = 7
message_key[1] = 4
message_key[2] = 11
message_key[3] = 11
message_key[4] = 14

message_0 = (message_key[0] + key) % 26
message_1 = (message_key[1] + key) % 26
message_2 = (message_key[2] + key) % 26
message_3 = (message_key[3] + key) % 26
message_4 = (message_key[4] + key) % 26

print('Cipher of hello is:',
      Caesar_cipher[message_0] +
      Caesar_cipher[message_1] +
      Caesar_cipher[message_2] +
      Caesar_cipher[message_3] +
      Caesar_cipher[message_4])