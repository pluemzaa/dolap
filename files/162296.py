data1 = []
data2 = []
while True:
    temp = input('Enter data example (x1,x2,x3 ...): ')
    if temp == 'exit':
        break
    x1 = temp.split(',')
    x1 = [float(x) for x in x1]
    data1.append(x1)
    label = input('Enter data example (y): ')
    data2.append(label)

y = input('Prediction, enter your input (x1,x2,x3 ...): ').split(',')
y = [float(x) for x in y]

min_diff = float('inf')
min_label = ''

for i in range(len(data1)):
    r = 0
    for m in range(len(data1[i])):
        diff = (data1[i][m] - y[m])**2
        r += diff 
    d = r ** 0.5

    if d < min_diff:
        min_diff = d
        min_label = data2[i]

print(f'Min Euclidean distance: {min_diff:.2f}')
print(f'Result : {min_label}')