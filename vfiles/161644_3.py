import math

X = []
y = []

while True:
    x_input = input("Enter data example (x1,x2,x3 ...): ")
    if x_input.lower() == "exit":
        break
    y_input = input("Enter data example (y): ")
    X.append([float(v) for v in x_input.split(',')])
    y.append(y_input)

x_predict = input("Prediction, enter your input (x1,x2,x3 ...): ")
x_predict_values = [float(v) for v in x_predict.split(',')]

min_dist = None
min_label = None

for features, label in zip(X, y):
    if len(features) == len(x_predict_values):
        dist = math.sqrt(sum((a - b) ** 2 for a, b in zip(features, x_predict_values)))
        if min_dist is None or dist < min_dist:
            min_dist = dist
            min_label = label

if min_dist is not None:
    print(f"Min Euclidean distance: {min_dist:.2f}")
    print(f"Predicted label: {min_label}")
else:
    print("No valid comparison could be made.")