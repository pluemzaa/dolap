v1 = input("Enter v1 (space-separated): ").split()
v2 = input("Enter v2 (space-separated): ").split()

v1 = [int(i) for i in v1]
v2 = [int(i) for i in v2]

dot_product = v1[0]*v2[0] + v1[1]*v2[1] + v1[2]*v2[2]

print("Dot product:", dot_product)