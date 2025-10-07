data = []
label = []
while True:
    nums = input('Enter data example (x1,x2,x3 ...): ')
    if nums == 'exit':
        break
    nums = nums.split(',')
    nums = [float(x) for x in nums]
    data.append(nums)
    lab = input('Enter data example (y): ')
    label.append(lab)
en = input('Prediction, enter your input (x1,x2,x3 ...): ')
en = en.split(',')
en = [float(x) for x in en]
min_diff = float('inf')
min_index = -1
for i in range(len(label)):
    v1 = data[i]
    s = 0
    for j in range(len(v1)):
        s += (v1[j] - en[j]) ** 2
    distance = s ** 0.5
    if distance < min_diff:
        min_diff = distance
        min_index = i
print(f"Min Euclidean distance: {min_diff:.2f}")
print("Result:", label[min_index])