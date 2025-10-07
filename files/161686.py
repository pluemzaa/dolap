import math

data = []
label = []

while True:
    nums = input("Enter data example (x1,x2,x3 ...): ")
    if nums == 'exit':
        break
    nums = nums.split(',')
    nums = [float(i) for i in nums]
    data.append(nums)
    lab = input('Enter data example (y): ')
    label.append(lab)

d = input('Prediction, enter your input (x1,x2,x3 ...): ')
d = d.split(',')
d = [float(i) for i in d]

min_diff = float('inf')
min_index = -1

for i in range(len(label)):
    v1 = data[i]
    if len(v1) != len(d):
        print(f"Error: Vector size mismatch with example #{i+1}")
        continue
    s = 0
    for j in range(len(v1)):
        s += (v1[j] - d[j]) ** 2
    distance = math.sqrt(s)
    if distance < min_diff:
        min_diff = distance
        min_index = i

if min_index != -1:
    print(f'Min Euclidean distance: {min_diff:.2f}')
    print(f'Result : {label[min_index]}')