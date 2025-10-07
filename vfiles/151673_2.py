x1=int(input("Enter v1 (space-separated):")) 
x2=int(input("Enter v2 (space-separated):")) 
x3=x1.split()
x3_1=x2.split()
x4=x1[0]
x4_1=x1[1]
x4_2=x1[2]
x4_3=x2[0]
x4_4=x2[1]
x4_5=x2[2]
calculate=x4[0]*x4_3[0]+ x4_1[1]*x4_4[1]+x4_2[2]*x4_5[2] 
print(f"Dot product:{calculate}")