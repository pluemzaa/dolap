v1_str = input('Enter v1 (space-separated): ')
v1_parts = v1_str.split()
v1 = []
for a in v1_parts: v1.append(int(a))

v2_str = input('Enter v2 (space-separated):' )
v2_parts = v2_str.split()
v2 = []
for a in v2_parts: v2.append(int(a))

res0 = v1[0] * v2[0]
res1 = v1[1] * v2[1]
res2 = v1[2] * v2[2]

res_list = [res0, res1, res2]

dot_prod_sum = res0 + res1 + res2

print('Dot product:', dot_prod_sum)