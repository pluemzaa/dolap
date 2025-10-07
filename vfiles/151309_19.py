x = input("Enter v1 (space-separated):")
x = x.split()
x = int(x)

y = input("Enter v2 (space-separated):")
y = y.split()
y = int(y)

a = (x[0] * y[0])
b = (x[1] * y[1])
c = (x[2] * y[2])

result = a+b+c
print(f"Dot product:", {result})