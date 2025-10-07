w = input("Enter numbers separated by commas: ")
w =w.split(",")

for i in range(0,len(w)):
    w[i] = int(w[i])

y = int(input("Enter number to search: "))
for h in range(0,len(w)):
    if y== w[h]:
        print(f"Found {y} at index {h}")    
    elif y not in w:
        print(f"No {y} found.")
        break