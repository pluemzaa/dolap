x = list(map(int, input("Enter a series of numbers separated by commas: ").split(',')))
m = max(x)
found = False

for i in x:
    if i == m and not found:
        print(f"{i} is the maximum value: True")
        found = True
    else:
        print(f"{i} is the maximum value: False")