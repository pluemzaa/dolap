x = list(map(int, input("Enter a series of numbers separated by commas: ").split(',')))
m = max(x)
for i in x:
    print(f"{i} is the maximum value: {i == m}")