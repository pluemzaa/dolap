e1 = input('Enter v1 (space-separated):')
e2 = input('Enter v2 (space-separated):')
e1 = e1.split(' ')
e2 = e2.split(' ')
e1[0] = int(e1[0])
e1[1] = int(e1[1])
e1[2] = int(e1[2])

e2[0] = int(e2[0])
e2[1] = int(e2[1])
e2[2] = int(e2[2])

r = (e1[0] * e2[0]) + (e1[1] * e2[1]) + (e1[2]* e2[2])

print(f'Dot product: {r}')