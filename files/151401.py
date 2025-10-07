v1_str = (input("Enter v1 (space-separated):"))
v2_str = (input("Enter v2 (space-separated):"))
v1 = v1_str.split(" ")
v2 = v2_str.split(" ")
v1[0] = int(v1[0])
v1[1] = int(v1[1])
v1[2] = int(v1[2])

v2[0] = int(v2[0])
v2[1] = int(v2[1])
v2[2] = int(v2[2])

sum1 = v1[0] * v2[0]
sum2 = v1[1] * v2[1]
sum3 = v1[2] * v2[2]
Dot_product = sum1 + sum2 + sum3
print("Dot product: ", Dot_product)