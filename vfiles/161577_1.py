data = []
label = []

while True:
    nums = input("Enter Vector : ")
    
    if nums == "exit":
        break
    
    nums = [float(x) for x in nums.split(",")]
    
    data.append(nums)
    
    lab = input("Enter Pet : ")
    
    label.append(lab)
    
print(data,label)

feat = input("Enter Feat: ")
feat = [float(x) for x in feat.split(",")]

min_diff = float("inf")
min_i = -1

for i in range(len(label)):
    v1 = data[i]
    s = 0
    
    for j in range(len(v1)):
        s = s + abs(v1[j] - feat[j])
    
    print(i,s)
    
    if s < min_diff:
        min_diff = s
        min_i = i
        
print("min_index =",min_i)
print("Answer :",label[min_i])