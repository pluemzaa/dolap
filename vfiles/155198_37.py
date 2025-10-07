x = input("Enter a series of numbers separated by commas: ")
print()
x = list(map(int, x.split(',')))
m = max(x)
for i in x:
    print(f"{i} is the maximum value: {str(i == m)}")