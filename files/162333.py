import math  

feature = []
label = []
while True:
    nums_input = input("Enter data example (x1,x2,x3 ...): ")
    if nums_input == "exit":
        break
    
    nums_input_list = nums_input.split(",")
    nums_input_list = [int(x) for x in nums_input_list]
   
    
    feature.append(nums_input_list)
    lab = input("Enter data example (y): ")
    label.append(lab)

test_input = input("Prediction, enter your input (x1,x2,x3 ...): ")
test_point = [int(x) for x in test_input.split(",")]


min_dist = None
min_index = None
for i in range(len(feature)):
    dist = 0
    for j in range(len(feature[i])):
        dist += (test_point[j] - feature[i][j]) ** 2
    dist = math.sqrt(dist)
    if (min_dist is None) or (dist < min_dist):
        min_dist = dist
        min_index = i

print("Min Euclidean distance: %.2f" % min_dist)
print("Result :", label[min_index])