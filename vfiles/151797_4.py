#print('Hello Python!')
code = {'''
"Dog": 0,
"Cat": 1,
"Fish": 2
 '''
}
text = input("Enter your pets: ")
pets = text.split(",")
result = []
for i in pets:
    result.append(str(code[i]))
print("Code of your pets:", ",".join(result))