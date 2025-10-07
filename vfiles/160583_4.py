x = input("Enter a series of numbers separated by commas: ")
x = x.split(',')

max = int(x[0])
y = False

for i in x[1:]:
    n = int(i)
    if n > max:
        maximum = n
        print(f"set the maximum value to {max}")
        y = True
        
if not y:
    print(f"set the maximum value to {max}")

print(f"The maximum value is {max}")