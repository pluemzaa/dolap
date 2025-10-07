v1 = input('Enter v1 (space-separated): ')
v2 = input('Enter v2 (space-separated): ')
lv1 = v1.split(" ")
lv2 = v2.split(" ")
lv1[0] = int(lv1[0])
lv1[1] = int(lv1[1])
lv1[2] = int(lv1[2])

lv2[0] = int(lv2[0])
lv2[1] = int(lv2[1])
lv2[2] = int(lv2[2])
result = lv1[0]*lv2[0]+lv1[1]*lv2[1]+lv1[2]*lv2[2]
print(f'Dot product: {result}')