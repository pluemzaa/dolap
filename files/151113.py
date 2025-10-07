a = (input("Enter v1 (space-separated): "))
b = (input("Enter v2 (space-separated): "))
a = a.split(' ')
b = b.split(' ')
c0 = int(a[0])*int(b[0])
c1 = int(a[1])*int(b[1])
c2 = int(a[2])*int(b[2])
cal = c0+c1+c2

print(f"Dot product: {cal}")