V1=input('Enter v1(space-separated): ')
V2=input('Enter v2(space-separated): ')

V1_str= (len(V1))
V1_str=int
V1_0=V1_str(V1[0])
V1_1=V1_str(V1[1])
V1_2=V1_str(V1[2])

V2_str= (len(V2))
V2_str=int
V2_0=V2_str(V2[0])
V2_1=V2_str(V2[1])
V2_2=V2_str(V2[2])

Result_0=V1_0*V2_0
Result_1=V1_1*V2_1
Result_2=V1_2*V2_2

Total= Result_0+Result_1+Result_2

print('Dot product:',Total)