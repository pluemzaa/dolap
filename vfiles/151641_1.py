a_str=input('Enter v1 (space-separated):')
b_str=input('Enter v2 (space-separated):')
aw=a_str.split(' ')
aw[0]=int(a[0])
aw[1]=int(a[1])
aw[2]=int(a[2])
b=b_str.split(' ')
b[0]=int(b[0])
b[1]=int(b[1])
b[2]=int(b[2])
c=[0,0,0]
c[0]=aw[0]*b[0]
c[1]=aw[1]*b[1]
c[2]=aw[2]*b[2]
print("Dot product:",c[0]+c[1]+c[2])