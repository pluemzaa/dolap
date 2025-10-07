a=input("Enter v1 (space-separated):")
b=input("Enter v2 (space-separated):")
a=a.split(' ')
a[0]=int(a[0])
a[1]=int(a[1])
a[2]=int(a[2])
b=b.split(' ')
b[0]=int(b[0])
b[1]=int(b[1])
b[2]=int(b[2])
c=[0,0,0]
c[0]=a[0]*b[0]
c[1]=a[1]*b[1]
c[2]=a[2]*b[2]
print("Dot product:",c[0]+c[1]+c[2])