num = input('Enter numbers separated by commas: ')
Snum = int(input("Enter number to search: "))
num = num.split(",")
i = 0

for i in range(len(num)):
    num[i] = int(num[i])
    
for i in range(len(num)):
    if Snum == num[i]:
        print("Found ", Snum , " at index ", i)
        
if Snum not in num:
    print("No ", Snum," found.")