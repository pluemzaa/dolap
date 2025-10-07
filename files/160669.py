num  = input("Enter a series of numbers separated by commas:")
num = num.split(",")
for i in range(len(num)):
    num[i] = int(num[i])
max=num[0]
min=num[0]
for i in range(len(num)):
    if num[i]>max:
        max=num[i]
for i in range(len(num)):
    if num[i]<min:
        min=num[i]
print("Normalized values:")
s = 0
for i in range(len(num)):
    s = (num[i]-min)/(max-min)
    print(f"{s:.2f}")