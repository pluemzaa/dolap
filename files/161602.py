data =[]
lable = []
brbr = []
while True:
    nums = input('enter vector:')
    if nums=='exit':
        break
    nums = nums.split(',')
    nums = [float(x) for x in nums]
    # add data
    data.append(nums)
    lab = input('Enter label:')
    lable.append(lab)
    
print(data)
print(lable)
min_diff = float('inf')
min_index = -1
feat = input('enter feat: ')
feat = feat.split(',')
feat = [float(x) for x in feat]

for i in range(len(lable)):
    v1 = data[i]
    for j in range(len(v1)):
        s = s + abs(v1[j] - feat[j])
    print(i,'diff',s)
    if s < min_diff:
        min_diff = s
        min_index = i
    
# brbr.append(feat)







# Enter vector:

# 10,20,30

# Enter label :

# cat

# Enter vector:

# 1,2,3

# Enter label

# : dog

# Enter vector:

# 1.1,2.5,3.5

# Enter label:

# dog

# Enter vector:

# 10.1,20.5,30.5

# Enter label :

# cat

# Enter vector:

# exit

# Enter unk vector:

# 2,3,5

# Predicted label :

# cat