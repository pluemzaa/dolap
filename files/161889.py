import math

def euclidean_distance(p, q):
    if len(p) != len(q):
        return None
    sum_squares = 0
    for i in range(len(p)):
        sum_squares += (p[i] - q[i]) ** 2
    return math.sqrt(sum_squares)

X = []
y = []

while True:
    x_input = input("Enter data example (x1,x2,x3 ...): ")
    if x_input.lower() == "exit":
        break
    label = input("Enter data example (y): ")
    features = [float(x) for x in x_input.split(",")]
    X.append(features)
    y.append(label)

x_pred_input = input("Prediction, enter your input (x1,x2,x3 ...): ")
x_pred = [float(x) for x in x_pred_input.split(",")]

min_distance = None
predicted_label = None

for i in range(len(X)):
    dist = euclidean_distance(x_pred, X[i])
    if dist is None:
        print("Error: Input vector and sample vector must have the same size")
        exit()
    if (min_distance is None) or (dist < min_distance):
        min_distance = dist
        predicted_label = y[i]

print(f"Min Euclidean distance: {min_distance:.2f}")
print(f"Result : {predicted_label}")