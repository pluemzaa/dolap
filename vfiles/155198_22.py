x = list(map(int, input("Enter a series of numbers separated by commas: ").split(',')))
m = max(x)
for i in x:
    print(str(i) + " is the maximum value: " + ("True" if i == m else "False"))