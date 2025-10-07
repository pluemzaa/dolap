v1 = [int(i) for i in input("Enter v1: ").split()]
v2 = [int(i) for i in input("Enter v2: ").split()]

dot_product = 0
for i in range(len(v1)):
  dot_product += v1[i] * v2[i]

print(f"Dot product of v1 and v2 is: {dot_product}")