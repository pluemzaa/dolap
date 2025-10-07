num = input("Enter a series of numbers separated by commas: ")
num1 = num.split(",")
for i in range(len(num1)):
    num1[i] = int(num1[i])

min = num1[0]
max = num1[0]
for i in range(len(num1)):
    if num1[i] < min:
        min = num1[i]
    if num1[i] > max:
        max = num1[i]

print("Normalized values:")
for i in range(len(num1)):
    s = (num1[i] - min) / (max - min)
    print(f"{s:.2f}")