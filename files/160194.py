num = input("Enter numbers separated by commas: ")
num = num.split(",")
sea = int(input("Enter number to search: "))
i = 0
for i in range(len(num)) :
    num[i] = int(num[i])


for i in range(len(num)) :
    if sea == num[i] :
        print(f"Found {sea} at index  {i}")

if sea not in num :
    print(f"No {sea} found.")