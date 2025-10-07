row = int(input('Enter the number of rows for the pyramid: '))
box = (row*(row+1))/2
print('The total number of boxes: %.0f' %box)
print('The total number of boxes is ', end='')
r = 0
if box % 2 == 0:
    print('even')
    r = range(1, row+1)
else:
    print('odd')
    r = range(row, 0, -1)
        
for i in r:
    print(f'{i} '*i)