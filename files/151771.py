v1_str = input("Enter v1 (space-separated): ")
v2_str = input("Enter v2 (space-separated): ")

v1 = list(map(int, v1_str.split()))
v2 = list(map(int, v2_str.split()))

x0 = v1[0] * v2[0]
x1 = v1[1] * v2[1]
x2 = v1[2] * v2[2]

dot_product = x0 + x1 + x2

print("Dot product:", dot_product)