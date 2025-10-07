import math

data = []  
label = [] 

while True:
    nums = input('Enter data example (x1,x2,x3 ...):')
    if nums == 'exit':
        break
    nums = nums.split(',')
    nums = [int(x) for x in nums]
    data.append(nums)

    lab = input('Enter data example (y):')
    label.append(lab)

feat = input('Prediction, enter your input (x1,x2,x3 ...):')
feat = feat.split(',')
feat = [int(x) for x in feat]

min_diff = float('inf')  
min_index = -1           

for i in range(len(data)): 
    v = data[i]
    s = 0
    for j in range(len(v)):
        s += (v[j] - feat[j])**2
    
    current_distance = math.sqrt(s) 

    if current_distance < min_diff: 
        min_diff = current_distance
        min_index = i

print(f'Min Euclidean distance: {min_diff:.2f}')
print(f'Result : {label[min_index]}')