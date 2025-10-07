a = input("Enter v1 (space-separated):")
a = a.split(" ")
a = int(a[0])
a = int(a[1])
a = int(a[2])
b = int(input("Enter v2 (space-separated):"))
b = b.split(" ")
b = int(b[0])
b = int(b[1])
b = int(b[2])


c0 = a[0] * b[0]
c1 = a[1] * b[1]
c2 = a[2] * b[2]

c = [c0,c1,c2]
d = c[0] + c[1] + c[2]
print("Dot product",d)