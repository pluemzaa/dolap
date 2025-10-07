import math

data = []
label = []
while True:
    nums = input('Enter data example (x1,x2,x3 ...): ')
    if nums == 'exit':
        break
    
    nums = nums.split(",")
    nums = [float(x) for x in nums]
    data.append(nums)
    
    lab = input('Enter data example (y): ')
    label.append(lab)

feat = input('Prediction, enter your input (x1,x2,x3 ...): ')
feat = feat.split(",")
feat = [float(x) for x in feat]

min_dis = float('inf')
res = None

for i in range(len(data)):
    s = 0
    for j in range(len(data[i])):
        diff = data[i][j] - feat[j]
        s += diff ** 2
    
    distance = math.sqrt(s)
    
    if distance < min_dis:
        min_dis = distance
        res = label[i]

print(f"Min Euclidean distance: {min_dis:.2f}")
print(f"Result : {res}")