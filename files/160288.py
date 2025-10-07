num  = input("Enter a series of numbers separated by commas:")
num = num.split(",")
for i in range(len(num)):
    num[i] = int(num[i])
max=num[0]
for i in range(len(num)):
    if num[i]>max:
        max=num[i]
        print("set the maximum value to",max)
        continue
    i+=1
print("The maximum value is",max)