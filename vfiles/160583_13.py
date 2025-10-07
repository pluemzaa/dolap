x = input("Enter a series of numbers separated by commas: ")
x = x.split(',')

maximum = int(x[0])
showed = False

i = 1
while i < len(x):
    n = int(x[i])
    if n > maximum:
        maximum = n
        print("set the maximum value to", maximum)
        showed = True
    i += 1
        
if not showed:
    print("set the maximum value to", maximum)

print("The maximum value is ", maximum)