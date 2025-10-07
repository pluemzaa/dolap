data = []
label = []
while True:
    nums = input(’Enter vector: ‘)
    if nums == ’:exit‘:
        break
    nums = nums.split(’, ‘)
    nums = [float(x) for x in nums]
    data.append(nums)

    lab = input(’Enter label: ‘)
    label.append(lab)

print(data)
print(label)

en = input(’Enter input: ‘)
en = en.split(’,‘)
en = [float(x) for x in en]
min_diff = float(’inf‘)
min_index = -1
for i in range(len(label)):
    v1 = data[i]
    s = 0
    for j in range(len(v1)):
        s = s + abs(v1[j] - en[j])
    print(i, diff:=s)
    if s < min_diff:
        min_diff = s
        min_index = i
print(”min_index=“, min_index)
print(”Answer : “, label[min_index])