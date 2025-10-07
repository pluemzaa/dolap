num1 = input("Enter v1 (space-separated):")
num2 = input("Enter v2 (space-separated):")
x1 = num1.split(" ")
x2 = num2.split(" ")
x1[0] = int(x1[0])
x1[1] = int(x1[1])
x1[2] = int(x1[2])

x2[0] = int(x2[0])
x2[1] = int(x2[1])
x2[2] = int(x2[2])

z0 = (x1[0]*x2[0])
z1 = (x1[1]*x2[1])
z2 = (x1[2]*x2[2])



xy = z0+z1+z2


print("Dot product" ,xy)