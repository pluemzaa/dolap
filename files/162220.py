import math

X = []
y = []

while True:
    data = input("Enter data example (x1,x2,x3 ...): ")
    if data.lower() == "exit":
        break
    label = input("Enter data example (y): ")
    X.append([float(v) for v in data.split(",")])
    y.append(label)

X_input = [float(v) for v in input("Prediction, enter your input (x1,x2,x3 ...): ").split(",")]

min_dist = None
min_label = None

for i in range(len(X)):
    dist = math.sqrt(sum((X[i][j] - X_input[j])**2 for j in range(len(X[i]))))
    if min_dist is None or dist < min_dist:
        min_dist = dist
        min_label = y[i]

print(f"Min Euclidean distance: {min_dist:.2f}")
print(f"Result : {min_label}")