import math

X = []
y = []
while True:
    x_input = input("Enter data example (x1,x2,x3 ...): ")
    if x_input.lower() == "exit":
        break
    label = input("Enter data example (y): ")
    features = [int(v.strip()) for v in x_input.split(",")]
    X.append(features)
    y.append(label)
dn = input("Prediction, enter your input (x1,x2,x3 ...): ")
fn = [int(v.strip()) for v in dn.split(",")]


if any(len(sample) != len(fn) for sample in X):
    print("Error: All vectors must have the same size")
else:
    min_distance = None
    predicted_label = None


    for i in range(len(X)):
        d = 0
        for j in range(len(X[i])):
            d += (X[i][j] - fn[j]) ** 2
        distance = math.sqrt(d)
        if min_distance is None or distance < min_distance:
            min_distance = distance
            predicted_label = y[i]


    print(f"Min Euclidean distance: {min_distance:.2f}")
    print(f"Result : {predicted_label}")