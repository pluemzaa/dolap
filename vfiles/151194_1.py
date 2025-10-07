a = int(input("Enter v1 (space-separated):"))
b = int(input("Enter v2 (space-separated):"))

a = a.split(" ")
b = b.split(" ")

c0 = a[0] * b[0]
c1 = a[1] * b[1]
c2 = a[2] * b[2]

c = [c0,c1,c2]
d = c[0] + c[1] + c[2]
print("Dot product",d)