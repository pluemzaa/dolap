data=[]
label=[]
while True:
    nums=input("Enter vector: ")
    if nums =="exit":
        break
    nums = nums.split(",")
    nums = [float(x) for x in nums]
    #add data
    data.append(nums)
    
    lab=input("Enter label: ")
    label.append(lab)
print(data)
print(label)

feat=input("Enter feat:")
feat=feat.split(",")
feat=[float(x) for x in feat]
min_diff = float("inf")
min_index = -1
for i in range(len(label)):
    v1=data[i]
    s=0
    for j in range(len(v1)):
        s = s+abs(v1[j]-feat[j])
    print(i,"diff=",s)
    if s < min_diff:
        min_diff = s
        min_index = i
print("min_index=",min_index)
print("Answer:",label[min_index])

#1,2,3
#3,5,4
#6,1,4