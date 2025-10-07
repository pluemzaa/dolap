x = input("Enter a series of numbers separated by commas: ")
print()
x = x.split(',')
for i in x:
    print(i + " is the maximum value: " + (("True" if int(i) == max(map(int, x)) else "False")))