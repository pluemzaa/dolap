x = input("Enter a series of numbers separated by commas: ")
print()
x = x.split(",")
m = max(map(int, x))
for i in x:
    print(i + " is the maximum value: " + ((int(i) == m) and "True" or "False"))