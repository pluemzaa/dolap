#Enter a : 1 2 3 
#Enter b : 4 5 6
a_int = input('Enter a:')
a = a_int.split(' ')
a[0] = int(a[0])
a[1] = int(a[1])
a[2] = int(a[2])
print(a)
b = [4,5,6]
total = a[0]*b[0] + a[1]*b[1] + a[2]*b[2]
total= a[0]*b[0] + a[1]*b[1] + a[2]*b[2]
print(total)