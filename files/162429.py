data = [] # [[10,20,30],[1,2,3]]
label = [] # ['cat','dog']
while True:
    x = input('Enter data example (x1,x2,x3 ...): ')
    if x=='exit':
        break
    x = x.split(',')
    x = [float(x) for x in x]
    data.append(x)

    y = input('Enter data example (y): ')
    if y=='exit':
        break
    label.append(y)

x_input = input('Prediction, enter your input (x1,x2,x3 ...): ')
x_input = x_input.split(',')
x_input = [float(x) for x in x_input]
min_diff = float('inf')
min_index = -1

for i in range(len(label)):
    v = data[i]
    sum = 0
    if len(v) != len(x_input):
        print('Error: Vectors must have the same size')
    else:
        for j in range(len(v)):
            sum += abs((x_input[j] - v[j]) ** 2)
        sum_all = (sum ** 0.5)
        if sum_all < min_diff:
            min_diff = sum_all
            min_index = i
print(f"Min Euclidean distance: {min_diff:.2f}")
print(f"Result : {label[min_index]}")