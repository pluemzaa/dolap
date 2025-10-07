data = []
label = []
while True:
    nums = input("Enter vector:")
    if nums == 'exit':
        break
    nums = nums.split(',')
    nums = [int(x) for x in nums]
    data.append(nums)

    lab = input("Enter lable:") 
    label.append(lab)
print(data)
print(label)
feat = input("Enter feat:")
feat = feat.split(',')
feat = [int(x) for x in feat]
min_diff = float('inf')
min_index = -1
for i in range(len(label)):
    v = data[i]
    s = 0
    for j in range(len(v)):
        s = s + abs(v[j] - feat[j])
    print(i,'diff=',s)
    if s < min_diff:
        min_diff = s
        mim_index = i
print('min_diff=',min_diff)
print('min_index=',min_index)
print('answer=',label[min_index])