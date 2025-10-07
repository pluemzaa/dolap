message = input('Enter input: ')
translate = ''
i = len(message) - 1
while i >= 0:
  translate += message[i]
  i = i - 1
print(translate)