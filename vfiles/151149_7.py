a = input('Enter v1 (space-separated):')
a = a.split(' ')
a[0] = int(a[0])
a[1] = int(a[1])
a[2] = int(a[2])

b = input('Enter v2 (space-separated):')
b = b.split(' ')
b[0] = int(a[0])
b[1] = int(a[1])
b[2] = int(a[2])

dot = (a[0]*b[0])+(a[1]*b[1])+(a[2]*b[2])
print(f"Dot product:{dot}")