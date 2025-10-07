data = []
label =  [] 

while True:    
    nums = input("Enter data example (x1,x2,x3 ...): ")
    if nums == 'exit':
        break

    nums = nums.split(',')
    nums = [float(x) for x in nums]
    data.append(nums)
    
    lab = input("Enter data example (y): ")
    label.append(lab)



feat = input("Prediction, enter your input (x1,x2,x3 ...): ")
feat = feat.split(',')
feat = [float(x) for x in feat]

min_diff = float("inf")
min_index = -1

for i in range(len(label)):
    v = data[i]
    sum = 0
    for j in range(len(v)):
        sum = sum + (abs(v[j] - feat[j]) ** 2)
    
    d = (sum) ** (1/2)
    
    if d < min_diff:
        min_diff = d 
        min_index = i 
        
print(f"Min Euclidean distance: {min_diff:.2f}")
print('Result : ',label[min_index])



# [[10, 20, 30], [10, 20, 25], [10, 20, 30], [1, 2, 3], [2, 2, 2]]
# ['cat', 'cat', 'cat', 'dog', 'dog']