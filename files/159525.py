text = input("Enter input:")
result = ""
for x in range(len(text) -1,-1,-1):
  result += text[x]
print(result)