import math

list_data_x = []
list_data_y = []

while True:
    data_x1 = input('Enter data example (x1,x2,x3 ...):')
    if data_x1 == 'exit':
        break
    data_x = data_x1.split(',')
    for x in range(len(data_x)):
        data_x[x] = int(data_x[x])
    data_y = input('Enter data example (y):')

    list_data_x.append(data_x)
    list_data_y.append(data_y)

predic = [int(z) for z in input('Prediction, enter your input (x1,x2,x3 ...):').split(',')]

_sum_data = []
for i in range(len(list_data_x)):
    _sum = 0
    for j in range(len(list_data_x[i])):
        d = ((predic[j] - list_data_x[i][j]) ** 2 )
        _sum += d
    _sqr = math.sqrt(_sum)
    _sum_data.append(_sqr)


_min_data = _sum_data[0]
_min_data_y = list_data_y[0]

for i in range(len(list_data_x)):
    if _sum_data[i] < _min_data:
        _min_data = _sum_data[i]
        _min_data_y = list_data_y[i]



print('Min Euclidean distance :%.2f'%_min_data)
print('Result :',_min_data_y)