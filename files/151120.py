v1=input("Enter v1 (space-separated):")
v2=input("Enter v2 (space-separated):")
v = v1.split(' ')
vv =v2.split(' ')
v[0]=int(v[0])
v[1]=int(v[1])
v[2]=int(v[2])
vv[0]=int(vv[0])
vv[1]=int(vv[1])
vv[2]=int(vv[2])

c0=vv[0]*v[0]
c1=vv[1]*v[1]
c2=vv[2]*v[2]

sum=c0+c1+c2
print(f"Dot product: {sum}")