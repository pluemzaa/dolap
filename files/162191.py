data = []
label = []
while True:
    nums = input('Enter data example (x1,x2,x3 ...): ')
    if nums == 'exit':
        break
    nums = nums.split(',')
    nums = [int(x) for x in nums]
    data.append(nums)

    lab = input('Enter data example (y): ')
    label.append(lab)

feat = input('Prediction, enter your input (x1,x2,x3 ...): ')
feat = feat.split(',')
feat = [int(x) for x in feat]

min_distance = float('inf')
predicted_label = -1
for i in range(len(label)):
    v = data[i]
    dist = 0
    for j in range(len(v)):
        dist = sum((a-b)**2 for a,b in zip(v,feat))**0.5
    if dist < min_distance:
        min_distance = dist
        predicted_label = i
print(f'Min Euclidean distance: {min_distance:.2f}')
print('Result :' ,label[predicted_label])