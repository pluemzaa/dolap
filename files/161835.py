import math
data_points = []
labels = []
while True:
    x_str = input("Enter data example (x1,x2,x3 ...): ")
    if x_str.lower() == "exit":
        break
    x_values = list(map(float, x_str.split(",")))
    y_label = input("Enter data example (y): ")
    data_points.append(x_values)
    labels.append(y_label)
test_str = input("Prediction, enter your input (x1,x2,x3 ...): ")
test_values = list(map(float, test_str.split(",")))

min_distance = None
predicted_label = None

for i, point in enumerate(data_points):
    dist = math.sqrt(sum((a - b) ** 2 for a, b in zip(test_values, point)))
    
    if min_distance is None or dist < min_distance:
        min_distance = dist
        predicted_label = labels[i]

print(f"Min Euclidean distance: {min_distance:.2f}")
print(f"Result : {predicted_label}")