X = input("Enter v1 (space-separated): ")
V = input("Enter v2 (space-separated): ")

Xer = X.split(" ")
Vr = V.split(" ")

Xer[0] = int(Xer[0])
Xer[1] = int(Xer[1])
Xer[2] = int(Xer[2])
# print(Xer)

Vr[0] = int(Vr[0])
Vr[1] = int(Vr[1])
Vr[2] = int(Vr[2])
# print(Vr)

r0 = Xer[0]*Vr[0]#1*4
# r1 = Xer[1]*Vr[1]
# r2 = Xer[2]*Vr[2]

# k0 = r0 + Vr[0]
# print(k0)
# k1 = k0 + Vr[2]
# k2 = r2 + Vr[2]
m0 =  Xer[1]* Vr[1]#2*5

c0 = Xer[2] * Vr[2]#3*6

p0 = r0 + m0
p1 = p0 + c0

# print(p0)
print(f"Dot product: {p1}")


# print(r0)
# print(l0)
# print(m0)
# print(c0)
# print(r2)