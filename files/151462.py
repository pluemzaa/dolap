v1_int = input("Enter v1 (space-separated): ")
v1= v1_int.split( )
v2_int = input("Enter v2 (space-separated): ")
v2 = v2_int.split( )

v1[0]=int(v1[0])
v1[1]=int(v1[1])
v1[2]=int(v1[2])

v2[0]=int(v2[0])
v2[1]=int(v2[1])
v2[2]=int(v2[2])

print("Dot product:",(v1[0]*v2[0])+(v1[1]*v2[1])+(v1[2]*v2[2]) )