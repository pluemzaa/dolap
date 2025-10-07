num = input("Enter a series of numbers separated by commas: ")
num = num.split(",")

for i in range(0,len(num)):
    num[i] = int(num[i])

Max = max(num)
Min = min(num)
print("Normalized values:")
for i in num:
    print((i-min(num))/(max(num)-min(num)))