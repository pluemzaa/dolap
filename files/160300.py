num = input("Enter numbers separated by commas: ")
num = num.split(",")
nums = int(input("Enter number to search: "))
f = False
for i in range(0,len(num)):
    num[i] = int(num[i])

for i in range(0,len(num)):
    if nums == num[i]:
        print("Found ",nums," at index ",i)
        f = True

if f == False:
    print("No ",nums," found.")