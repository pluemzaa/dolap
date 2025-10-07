v1_str = input("Enter v1 (space-separated): ")
v2_str = input("Enter v2 (space-separated): ")

v1 = v1_str.split(' ')
v2 = v2_str.split(' ')

Dot_product = (int(v1[0]) * int(v2[0]) + int(v1[1]) * int(v2[1]) + int(v1[2])*  int(v2[2]))

print("Dot product: ",Dot_product, end=' ')