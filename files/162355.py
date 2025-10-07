import math

X = []
y = []

while True:
    x_input = input("Enter data example (x1,x2,x3 ...): ")
    if x_input.lower() == "exit":
        break
    X.append([float(i) for i in x_input.split(",")])
    y_label = input("Enter data example (y): ")
    y.append(y_label)

X_input = [float(i) for i in input("Prediction, enter your input (x1,x2,x3 ...): ").split(",")]

min_dist = None
min_label = None

for i in range(len(X)):
    dist = math.sqrt(sum((X_input[j] - X[i][j])**2 for j in range(len(X_input))))
    if min_dist is None or dist < min_dist:
        min_dist = dist
        min_label = y[i]

print(f"Min Euclidean distance: {min_dist:.2f}")
print(f"Result : {min_label}")