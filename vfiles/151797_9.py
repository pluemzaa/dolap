#print('Hello Python!')
code = {
"Dog": 2,
"Cat": 2,
"Fish": 1
}
text = input("Enter your pets: ")
pets = text.split(",")
result = []
for i in pets:
    result.append(str(code[i]))
print("Code of your pets:", ",".join(result))