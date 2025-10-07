codes = {'Dog': 0, 'Cat': 1, 'Fish': 2}

text = input("Enter your pets: ")
data = text.split(',')

for i in range(len(data)):
    data[i] = data[i].strip()

result = []
for pet in data:
    result.append(str(codes[pet]))

print("Code of your pets:", ",".join(result))