x = input("Enter a series of numbers separated by commas: ")
x = x.split(",")
i = 0
maximum = x[0]
showed = False

i = 1 
while i < len(x):
    n = x[i]
    if n > maximum:
        maximum = n
        print(f"set the maximum value to {maximum}")
        showed = True
    i += 1

if not showed:
    print(f"set the maximum value to {maximum}")
print(f"The maximum value is {maximum}")