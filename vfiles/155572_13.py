v1 = input("Enter v1 (space-separated):")
v2 = input("Enter v2 (space-separated):")
Dp1 = v1.split (" ")
Dp2 = v2.split (" ")

Dp1[0] = int (Dp1[0])
Dp1[1] = int (Dp1[1])
Dp1[2] = int (Dp1[2])

Dp2[0] = int (Dp2[0])
Dp2[1] = int (Dp2[1])
Dp2[2] = int (Dp2[2])

r0 = Dp1[0]*Dp2[0]
r1 = Dp1[1]*Dp2[1]
r2 = Dp1[2]*Dp2[2]
r = [r0,r1,r2]
e1 = r0+r1+r2
print(f"Dot product:{e1}")