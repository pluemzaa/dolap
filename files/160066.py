message = input("Enter input: ")
reverse = ''
i = len(message) - 1
while i>=0:
    reverse+=message[i]
    i-=1
print(reverse)