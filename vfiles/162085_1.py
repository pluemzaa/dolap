data = [] #[[10,20,30],[11,20,30]]
label = [] # ['cat','cat']
while True:
    nums = input ('Enter vector:')
    if nums == 'exit':
        break
    nums = nums.split(',')
    nums = [int(x) for x in nums]  #[10,20,30]
    data.append(nums)
    lb = input ('Enter label:')
    label.append (lb)
print(data)
print(label)

feat = input('Enter new vector:')
feat = nums.split(',')
feat =[int(x) for x in feat]#[1,2,3]
min_diff = float('inf')
min_index = -1
for i in range(len(label)):
    v = data[i]
    d = 0
    for j in range(len(v)):
        d = d + abs(v[j]- feat[j])
    print(i, 'diff=',d)
    if d < min_diff:
        min_diff = d
        min_index = i
print('min_index = ',i)
print('min_diff = ',min_diff)
print('Answer : ',label[min_index])