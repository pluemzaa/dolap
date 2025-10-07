num = input("Enter numbers separated by commas:")
num = num.split(",")
nums = int(input("Enter number to search:"))
i = 0
for i in range(len(num)):
    num[i] = int(num[i])

for i in range(len(num)):
    if num[i] == nums :
        print(f"Found {nums} at index ",i)
    
print(f"No {nums} found.")