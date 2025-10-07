x = input("Enter v1 (space-separated):")
x = x.split()

y = input("Enter v2 (space-separated):")
y = y.split()

a = int(x[0]) * int(y[0])
b = int(x[1]) * int(y[1])
c = int(x[2]) * int(y[2])

data =[a,b,c]
result=a+b+c
print("Dot product:", result)