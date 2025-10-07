v1_input = input("Enter v1 (speace-separated):")
v1 = v1_input.split()
a = int(v1[0])
b = int(v1[1])
c = int (v1[2])

v2_input = input("Enter v2 (speace-separated):")
v2 = v2_input.split()
x = int(v2[0])
y = int(v2[1])
z = int(v2[2])

dot_product = (a * x) + (b * y) + (c * z)

print("Dot product:",dot_product)