text = input("Enter input: ")
reversed_text = ''
x = len(text) - 1
while x >= 0:
    reversed_text += text[x]
    x -= 1
print(reversed_text)