data = []
label = []

while True:
    nums = input('Enter data example (x1,x2,x3 ...): ')
    if nums == 'exit':
        break
    nums = [int(x) for x in nums.split(',')]
    data.append(nums)
    label.append(input('Enter data example (y): '))

feat = [int(x) for x in input('Prediction, enter your input (x1,x2,x3 ...): ').split(',')]

min_diff = float('inf')
min_index = -1

for i in range(len(data)):
    s = 0
    for j in range(len(data[i])):
        s += (data[i][j] - feat[j]) ** 2
    if s < min_diff:
        min_diff = s
        min_index = i
a = min_diff**0.5

print(f"Min Euclidean distance: {a:.2f}")
print("Result :", label[min_index])