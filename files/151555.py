a = input("Enter v1 (space-separated):")
b = input("Enter v2 (space-separated):")
a = a.split(' ')
b = b.split(' ')

a[0] = int(a[0])
a[1] = int(a[1])
a[2] = int(a[2])

b[0] = int(b[0])
b[1] = int(b[1])
b[2] = int(b[2])

#a = [1,2,3]
#b = [5,6,7]

c0 = a[0]*b[0]
c1 = a[1]*b[1]
c2 = a[2]*b[2]

#c = [c0, c1, c2]
#print(c)
_sum = c0+c1+c2
print("Dot product: %d"%(_sum))