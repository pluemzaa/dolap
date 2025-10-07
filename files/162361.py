import math

data = []
label = []
while True:
    nums = input("Enter data example (x1,x2,x3 ...): ")
    if nums == 'exit':
        break
    nums = nums.split(',')
    temp = []
    for i in nums:
        temp.append(float(i.strip()))
    data.append(temp)
    lab = input("Enter data example (y): ")
    label.append(lab)

if len(data) == 0:
    print('No examples entered.')
    exit()

Feat_str = input("Prediction, enter your input (x1,x2,x3 ...): ")
Feat = Feat_str.split(',')
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
        d = d + (diff ** 2)
    d = float(math.sqrt(d))
    if d < min_diff:
        min_index = i
        min_diff = d

print('Min Euclidean distance: %.2f' % min_diff)
print('Result :', label[min_index])