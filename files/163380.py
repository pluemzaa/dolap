items = []

for i in  range(4):
    item = input(f'Enter item {i+1} :')
    w = float(input(f'Enter weight {i+1} :'))
    
    items.append([item, w])

total = 0
for i in items:
    print(f'{i[0]}           {i[1]:.2f}')
    total += i[1]

print('---------------------------')
print('total           %.2f' %total)