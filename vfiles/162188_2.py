import math

X = []
y = []

while True:
    x_input = input("Enter data example (x1,x2,x3 ...): ")
    if x_input.lower() == "exit":
        break
        
    x_values = [float(num) for num in x_input.split(",")]
    label = input("Enter data example (y): ")
    
    X.append(x_values)
    y.append(label)

X_pred_input = input("Prediction, enter your input (x1,x2,x3 ...): ")
X_pred = [float(num) for num in X_pred_input.split(",")]

if any(len(x) != len(X_pred) for x in X):
    print("Error: All vectors must have the same size.")
else:
    min_distance = None
    min_label = None

    for features, label in zip(X, y):
        sum_sq = 0
        for xi, pi in zip(features, X_pred):
            sum_sq += (xi - pi) ** 2
        distance = math.sqrt(sum_sq)

        if (min_distance is None) or (distance < min_distance):
            min_distance = distance
            min_label = label

    print(f"Min Euclidean distance: {min_distance:.2f}")
    print(f"Result : {min_label}")