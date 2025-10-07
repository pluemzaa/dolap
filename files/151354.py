v1 = input("Enter v1 (space-separated): ").split()
v2 = input("Enter v2 (space-separated): ").split()

Sum = 0
for i in range(3):
    v1[i] = int(v1[i])
    v2[i] = int(v2[i])

    Sum += (v1[i]*v2[i])

print("Dot product:", Sum)