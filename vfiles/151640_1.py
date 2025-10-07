a1_str = input("Enter a1:")
a1 = a1_str .split('')
a1[0]
print(a1)
a1[0]=int(a1[0])
a1=[1,2,3]
b1=[5,6,7]

c0= a1[0]*b1[0]
c1= a1[1]*b1[1]
c2= a1[2]*b1[2]

c=[c0,c1,c2]
s=c0+c1+c2
print(c)
print(s)