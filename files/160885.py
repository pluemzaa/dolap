num = input("Enter a series of numbers separated by commas: ")
num = num.split(",")

for i in range(len(num)):
    num[i] = int(num[i])

max = max(num)
min = min(num)

print("Normalized values:")

for i in range(len(num)):
    all = (num[i]-min)/(max-min)
    print(f"{all:.2f}")