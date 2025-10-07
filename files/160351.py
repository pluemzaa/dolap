x = input("Enter numbers separated by commas: ")
y = x.split(",")
z = int(input("Enter number to search: "))

for i in range(len(y)):
    y[i] = int(y[i])
    
    
found = False
for i in range(len(y)):
    if y[i] == z:
        print(f"Found {z} at index {(i)}")
        found = True  

if not found:
    print("No",z,"found.")