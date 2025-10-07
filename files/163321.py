data = []
label = []
s = 0
while True :
    nums = input ('Enter data example (x1,x2,x3 ...): ')
    if nums == 'exit':
        break
    nums = nums.split(',')
    nums = [int(x) for x in nums]
    data.append(nums)
    lb = input('Enter data example (y): ')
    label.append(lb)
    

feat = input('Prediction, enter your input (x1,x2,x3 ...): ')
feat = feat.split(',')
feat = [int(x) for x in feat]
min_distance = float('inf')
min_index = -1

for i in range(len(label)):
    v = data[i]
    s = 0
    
    for j in range(len(v)):
        s += (abs(v[j] - feat[j])) ** 2
    d = s**0.5
    
    if d < min_distance:
        min_distance = d
        min_index = i
if min_index != -1 :
    print(f'Min Euclidean distance:  {min_distance:.2f}')
    print('Result : ', label[min_index])