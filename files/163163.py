lsf = []
lsw = []

for i in range(4):
    lsf.append(input(f"Enter item{i+1} : "))
    lsw.append(float(input(f"Enter weight{i+1} : ")))
x = 0
for i in range(4):
    print(f'{lsf[i]}        {lsw[i]:.2}')
    x += lsw[i]

print('---------------------------')
print(f'total       {x:.2f}')