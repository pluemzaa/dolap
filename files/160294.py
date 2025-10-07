a = input("Enter numbers separated by commas: ")
a = a.split(",")
b = int(input("Enter number to search: "))
for i in range(0,len(a)):
    a[i] = int(a[i])
    
for i in range(0,len(a)):
    if b == a[i]:
        print("Found",b,"at index",i)

if b not in a:
    print(f"No {b} found.")