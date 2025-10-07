n = input("Enter numbers separated by commas: ")
n = n.split(",")
y = input("Enter number to search: ")

if y in n:
    for i in range(len(n)):
        if n[i] == y:
            print(f"found {y} at index {i}")
else:
    print(f"No {y} found.")