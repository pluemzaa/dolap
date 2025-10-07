label = []  
data = []  

while True:
    nums = input("Enter data example (x1,x2,x3 ...): ")
    if nums == "exit":
        break

    nums = nums.split(",")
    nums = [int(x) for x in nums]


    data.append(nums)
    lab = input("Enter data example (y): ")
    label.append(lab)



feat = input("Prediction, enter your input (x1,x2,x3 ...): ")
feat = feat.split(",")
feat = [int(x) for x in feat]
min_diff = float("inf")
min_dist = float("inf")
min_index = -1

for i in range(len(label)):
    v = data[i]
    d = 0
    for j in range(len(v)):
        d += abs(v[j] - feat[j])
    if d < min_diff:
        min_diff = d
        min_index = i


for i in range(len(label)):
    v = data[i]
    d = 0
    for j in range(len(v)):
        d += (v[j] - feat[j])**2
    d = d**0.5
    if d < min_dist:
        min_dist = d
        min_index = i

print(f"Min Euclidean distance: {min_dist:.2f}")
print("Result :",label[min_index])