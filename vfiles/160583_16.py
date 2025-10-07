x = input("Enter a series of numbers separated by commas: ")
y = [int(x) for x in x.split(",")]

maximum = int(y[0])
showed = False

for i in y[1:]:
    n = int(i)
    if n > maximum:
        maximum = n
        print(f"set the maximum value to {maximum}")
        showed = True
        

if not showed:
    print(f"set the maximum value to {maximum}")

print(f"The maximum value is {maximum}")