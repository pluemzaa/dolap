import math
data = []
label = []
while True:
    nums = input("Enter data example (x1,x2,x3 ...): ")
    if nums == "exit":
        break
        
    nums = nums.split(",")
    nums = [float(x) for x in nums]
    data.append(nums)
    
    lb = input("Enter data example (y): ")
    label.append(lb)

feat = input("Prediction, enter your input (x1,x2,x3 ...): ")
feat = feat.split(",")
feat = [float(x) for x in feat]
min_diff = float("inf")
min_index = -1

for i in range(len(label)):
    v = data[i]
    d = 0
    for j in range(len(v)):
        d = d + abs(v[j] - feat[j])**2
    d = math.sqrt(d)
    if d < min_diff:
        min_diff = d
        min_index = i

print(f"Min Euclidean distance: {min_diff:.2f}")
print("Result :",label[min_index])