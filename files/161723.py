data=[]
label=[]
while True:
    nums=input("Enter data example (x1,x2,x3 ...): ")
    if nums =="exit":
        break
    nums = nums.split(",")
    nums = [float(x) for x in nums]
    #add data
    data.append(nums)
    
    lab=input("Enter data example (y): ")
    label.append(lab)
    

feat=input("Prediction, enter your input (x1,x2,x3 ...): ")
feat=feat.split(",")
feat=[float(x) for x in feat]
min_diff = float("inf")
best_index = -1
for i in range(len(data)):
    distance = 0
    for j in range(len(feat)):
        distance += (data[i][j] - feat[j])**2
    distance = distance**0.5
    
    if distance < min_diff:
        min_diff = distance
        best_index = i
print(f"Min Euclidean distance: {min_diff:.2f}")
print("Result : ",label[best_index])