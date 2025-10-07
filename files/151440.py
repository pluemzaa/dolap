v1_input = input("Enter v1 (space-separated): ")


v1_str_list = v1_input.split()


v1 = []
for s in v1_str_list:
  v1.append(int(s))

v2_input = input("Enter v2 (space-separated): ")
v2_str_list = v2_input.split()
v2 = []
for s in v2_str_list:
  v2.append(int(s))

dot_product = (v1[0] * v2[0]) + (v1[1] * v2[1]) + (v1[2] * v2[2])

print(f"Dot product: {dot_product}")