import math
X = []
y = []
while True:
    data = input("Enter data example (x1,x2,x3 ...): ")
    if data.lower() == "exit":
        break
    features = [float(i) for i in data.split(",")]
    label = input("Enter data example (y): ")
    X.append(features)
    y.append(label)
x_input = [float(i) for i in input("Prediction, enter your input (x1,x2,x3 ...): ").split(",")]
for i in range(len(X)):
    if len(X[i]) != len(x_input):
        print("Error: Vectors must have the same size")
        exit()
min_dist = None
min_label = None
for i in range(len(X)):
    dist = math.sqrt(sum((X[i][j] - x_input[j]) ** 2 for j in range(len(x_input))))
    if (min_dist is None) or (dist < min_dist):
        min_dist = dist
        min_label = y[i]
print(f"Min Euclidean distance: {min_dist:.2f}")
print(f"Result : {min_label}")