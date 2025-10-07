#Enter a : 1 2 3
#Enter b : 4 5 6
a_str = input('Enter a:')
a = a_str.split(' ')
a[0] =int(a[0])
a[1] =int(a[1])
a[2] =int(a[2])
print(a)
b = [4,5,6]
c0 = a[0]xb[0]
c1 = a[1]xb[1]
c2 = a[2]xb[2]
c =[c0, c1, c2]
Total = c0+c1+c2
print(Total)