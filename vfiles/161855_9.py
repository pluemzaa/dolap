data = []
label = []
while True:
    nums = input('Enter data example (x1,x2,x3 ...): ')
    if nums == 'exit':
        break
    nums = nums.split(',')
    temp = []
    for i in nums:
        temp.append(float(i.strip()))
    data.append(temp)
    lab = input('Enter data example (y): ')
    label.append(lab)

if len(data) == 0:
    print('No examples entered.')
    exit()

input_str = input('Prediction, enter your input (x1,x2,x3 ...): ')
Feat = input_str.split(',')
for i in range(len(Feat)):
    Feat[i] = float(Feat[i].strip())

min_diff = float('inf')
min_index = -1
for i in range(len(label)):
    v = data[i]
    if len(v) != len(Feat):
        print('Error: Vectors must have the same size')
        exit()
    d = 0
    for j in range(len(v)):
        diff = v[j] - Feat[j]
        d = d + (diff * diff)
    d = d ** 0.5
    print(i, 'diff =', round(d, 2))
    if d < min_diff:
        min_index = i
        min_diff = d

print('min_index =', min_index)
print('min_diff =', round(min_diff, 2))
print('answer =', label[min_index])