num_rows = int(input('Enter the number of rows for the pyramid: '))
total_boxes = (num_rows * (num_rows + 1)) / 2
print('The total number of boxes: %.0f' % total_boxes)
print('The total number of boxes is ', end='')
range = 0
if total_boxes % 2 == 0:
    print('even')
    range = range(1, num_rows + 1)
else:
    print('odd')
    range = range(num_rows, 0, -1)

for i in range:
    print(f'{i} ' * i)