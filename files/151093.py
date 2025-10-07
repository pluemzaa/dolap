a_str = input('Enter v1 (space-separated):')
b_str = input('Enter v2 (space-separated):')
a = a_str.split(' ')
b = b_str.split(' ')
a[0] = int(a[0])
a[1] = int(a[1])
a[2] = int(a[2])
b[0] = int(b[0])
b[1] = int(b[1])
b[2] = int(b[2])
c0 = a[0]*b[0]
c1 = a[1]*b[1]
c2 = a[2]*b[2]
_sum = c0+c1+c2
print("Dot product: %.0f"% (_sum))