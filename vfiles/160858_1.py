mess = input("Enter input: ")
translate = " "
i = len(mess) - 1
while i >= 0:
  translate += (mess[i])
  i = i - 1
print(translate)