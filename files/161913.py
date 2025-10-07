import math

data = []
label = []

while True:
    nums = input('Enter data example (x1,x2,x3 ...): ')
    if nums.lower() == 'exit':
        break
    nums = [float(x) for x in nums.split(',')]
    data.append(nums)
    
    lab = input('Enter data example (y): ')
    label.append(lab)

feat = input('Prediction, enter your input (x1,x2,x3 ...): ')
feat = [float(x) for x in feat.split(',')]

for v in data:
    if len(v) != len(feat):
        print("Error: All vectors must be of the same dimension.")
        exit()

min_diff = float('inf')
min_index = -1

for i in range(len(label)):
    v = data[i]
    sum_sq_diff = 0
    for j in range(len(v)):
        sum_sq_diff += (v[j] - feat[j]) ** 2

    distance = math.sqrt(sum_sq_diff)

    if distance < min_diff:
        min_diff = distance
        min_index = i

print(f"Min Euclidean distance: {min_diff:.2f}")
print('Result :', label[min_index])