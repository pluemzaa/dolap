message = input("Enter input:")
reverse = ""
i = len(message)-1
while i >= 0 :
  reverse = reverse + message[i]
  i = i - 1
print(reverse)