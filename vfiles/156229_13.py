A = [a-z]
key = int(input('Enter key: '))
cipher = input('A' + key) % 26
result = cipher
print('Cipher of hello is:', result)