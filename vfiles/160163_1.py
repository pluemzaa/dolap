x = input("Enter numbers separated by commas: ").split(',')
y = int(input("Enter number to search: "))
i = 0
while i < len(x):
    x[i] = int(x[i])
    i+=1
i=0
if y not in x :
    print(f"No {y} found.")
else :
    while i < len(x):
        if x[i] == y :
            print(f"Found {x[i]} at index {i}")
        i+=1