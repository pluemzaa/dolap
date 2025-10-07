data = []
label = []


while True:
    nums = input('Enter data example (x1,x2,x3 ...): ')
    if nums.lower() == "exit":
        break
    nums = [float(x.strip()) for x in nums.split(',')]
    data.append(nums)

    lab = input("Enter data example (y): ")
    label.append(lab)

feat = input('Prediction, enter your input (x1,x2,x3 ...): ')
feat = [float(x.strip()) for x in feat.split(',')]


min_diff = None
min_index = -1

for i in range(len(label)):
    v1 = data[i]
    
    if len(v1) != len(feat):
        print(f"Error: Vector size mismatch at example #{i+1}")
        continue

    s = 0
    for j in range(len(v1)):
        s += (v1[j] - feat[j]) ** 2 

    dist = s ** 0.5 


    if (min_diff is None) or (dist < min_diff):
        min_diff = dist
        min_index = i


if min_index != -1:
    print(f"Min Euclidean distance: {min_diff:.2f}")
    print("Result :", label[min_index])
else:
    print("No matching data to compare.")