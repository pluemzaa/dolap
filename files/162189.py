#lab4
import math
data = []
label = []

while True : 
    num = input("Enter data example (x1,x2,x3 ...): ")
    if num == 'exit': 
        break
    num = num.split(',')       
    num = [float(x) for x in num]
    data.append(num)

    lab = input("Enter data example (y): ")
    label.append(lab)

feat = input("Prediction, enter your input (x1,x2,x3 ...): ").split(",")
feat = [float(x) for x in feat]
min_diff = float('inf')
min_index = -1

for i in range(len(label)) :
    v1 = data[i]
    s = 0 
    for j in range(len(v1)) :
        s += (v1[j] - feat[j]) ** 2
    dis = math.sqrt(s)
    if dis < min_diff :
        min_diff = dis
        min_index = i 
print(f"Min Euclidean distance: {min_diff:.2f} ")
print("Result :",label[min_index])