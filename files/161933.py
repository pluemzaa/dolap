label = []
data_list = []
while True:
    data = input("Enter data example (x1,x2,x3 ...): ")
    if data.lower() == 'exit':
        break
    ex  = input("Enter data example (y): ")
    data = [float(x) for x in data.split(',')]
    data_list.append(data)
    label.append(ex)
feat = input("Prediction, enter your input (x1,x2,x3 ...): ")
feat = [float(f) for f in feat.split(',')]
min_index = 0
min_distance = None
for i in range(len(label)):
    diff_sum = 0
    for j in range(len(feat)):
        diff = feat[j] - data_list[i][j]
        diff_sum += diff ** 2
    distance = diff_sum ** 0.5

    if min_distance is None or distance < min_distance:
        min_distance = distance
        min_index = i

print(f"Min Euclidean distance: {min_distance:.2f}")
print(f"Result : {label[min_index]}")