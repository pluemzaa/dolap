v1 = list(map(int, input("Enter v1 (space-separated): ").split()))

v2 = list(map(int, input("Enter v2 (space-separated): ").split()))

dot_product = v1[0]*v2[0] + v1[1]*v2[1] + v1[2]*v2[2]
print("Dot product:", dot_product)