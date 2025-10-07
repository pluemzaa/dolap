v1_str=input("Enter v1 (space-separated):")
v2_str=input("Enter v2 (space-separated):")
v1=v1_str.split()
t1=int(v1[0])
t2=int(v1[1])
t3=int(v1[2])
v2=v2_str.split()
r1=int(v2[0])
r2=int(v2[1])
r3=int(v2[2])
s1=t1*r1
s2=t2*r2
s3=t3*r3
Total=s1+s2+s3
print("Dot product",Total)