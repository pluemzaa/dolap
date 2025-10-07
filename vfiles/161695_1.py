import math
data = []
lebel = []

while True:
    nums = input("Enter data example (x1,x2,x3 ...): ")
    if nums == 'exit':
        break
    nums = nums.split(',')
    nums = [float(x) for x in nums]
    data.append(nums)

    lab = input("Enter data example (y): ")
    lebel.append(lab)

feat = input("Prediction, enter your input (x1,x2,x3 ...): ")
feat = feat.split(',')
feat = [float(x) for x in feat]

min_diff = float('inf')
min_index = -1

for i in range(len(lebel)):
    d = math.sqrt(sum((data[i][j] - feat[j])**2 for j in range(len(feat))))
    if d < min_diff:
        min_diff = d
        min_index = i

print(f"Min Euclidean distance: {min_diff:.2f}")
print("Result:", lebel[min_index])