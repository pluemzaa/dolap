x = input("Enter a series of numbers separated by commas: ")
print()
x = x.split(",")
m = max(map(int, x))
for i in x:
    a = int(i) == m
    b = (a and "True") or "False"
    print(i + " is the maximum value: " + b)