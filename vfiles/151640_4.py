v1_str = input("Enter v1 : ")
v2_str = input("Enter v2 : ")

v1 = list(map(int, v1_str.split()))
v2 = list(map(int, v2_str.split()))

c0 = v1[0] * v2[0]
c1 = v1[1] * v2[1]
c2 = v1[2] * v2[2]

dot_product = c0 + c1 + c2

print("Dot product:", dot_product)