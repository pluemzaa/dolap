x = input("Enter a series of numbers separated by commas: ")
x = x.split(',')
y = list(map(int, x))

m = max(y)

for i in y:
    if i == m:
        print(f"{i} is the maximum value: True")
    else:
        print(f"{i} is the maximum value: False")