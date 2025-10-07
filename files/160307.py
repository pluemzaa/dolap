a = input("Enter a series of numbers separated by commas: ")
a = a.split(",")

for i in range(0,len(a)):
    a[i] = int(a[i])

max_s = a[0]
for i in range(len(a)):
    if a[i] > max_s:
        max_s = a[i]
        print("set the maximum value to",max_s)

print("The maximum value is ",max_s)