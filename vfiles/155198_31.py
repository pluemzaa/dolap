x = input("Enter a series of numbers separated by commas: ").split(',')
x = [int(i) for i in x]
m = max(x)
for i in x:
    print(f"{i} is the maximum value: {'True' if i == m else 'False'}")