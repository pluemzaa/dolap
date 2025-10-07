x = input("Enter v1 (space-separated):")
x = int(x)
x = x.split()

y = input("Enter v2 (space-separated):")
y = int(y)
y = y.split()

result = (x[0]*y[0]+x[1]*y[1]+x[2]*y[2])
print("Dot product:", result)