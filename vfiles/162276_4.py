data = []
label = []

while True:
    nums  = input("Enter data example (x1,x2,x3 ...): ")
    if nums == 'exit':
        break
    nums = nums.split(',')
    nums = [float(x) for x in nums]
    data.append(nums)

    lab = input("Enter data example (y): ")
    label.append(lab)

feat = input("Prediction, enter your input (x1,x2,x3 ...): ")
feat = feat.split(',')
feat = [float(x) for x in feat]

min_diff = float('inf')
min_index = -1
for i in range(len(label)):
    v = data[i]
    s = 0
    for j in range(len(v)):
        s = s + abs(v[j] - feat[j])**2
        s = s ** 0.5
    if s < min_diff:
        min_diff = s
        min_index = i

print(f"Min Euclidean distance: {s:.2f}")
print("Result : ",label[min_index])