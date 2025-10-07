a = input('Enter v1 (space-separated):')
a = a.split(' ')
a[0] = int(a[0])
a[1] = int(a[1])
a[2] = int(a[2])

b = input('Enter v2 (space-separated):')
b = b.split(' ')
b[0] = int(a[0])
b[1] = int(a[1])
b[2] = int(a[2])

c0 = a[0]+b[0]
c1 = a[1]+b[1]
c2 = a[2]+b[2]
c = [c0,c1,c2]
sum = c0+c1+c2
print("Dot product: "sum")