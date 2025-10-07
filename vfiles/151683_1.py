reaun = input("Enter v1 (space-separated):")
a = reaun("")
a[0] = int(a[0])
a[1] = int(a[1])
a[2] = int(a[2])
rose = input("Enter v2 (space-separated):")
b = rose("")
b[0] = int(b[0])
b[1] = int(b[1])
b[2] = int(b[2])
x = a[0] * b[0]
y = a[1] * b[1]
z = a[2] * b[2]
G = [x,y,z]
sum = x+y+z
print("Dot product:",sum)