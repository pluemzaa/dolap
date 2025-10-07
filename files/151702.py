v1_str = input('Enter v1 (space-separated):')
v1 = (v1_str.split(' '))

v2_str = input('Enter v2 (space-separated):')
v2 = (v2_str.split(' '))

r0 = int(v1[0]) * int(v2[0])
r1 = int(v1[1]) * int(v2[1])
r2 = int(v1[2]) * int(v2[2])
s = r0 + r1 + r2
print('Dot product:', s)