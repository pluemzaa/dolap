import math

def euclidean_distance(p, q):
    if len(p) != len(q):
        return None
    return math.sqrt(sum((p[i] - q[i]) ** 2 for i in range(len(p))))

X = []  # features
y = []  # label

while True:
    coords = input("Enter data example (x1,x2,x3 ...): ")
    if coords.lower() == "exit":
        break
    features = list(map(float, coords.split(",")))
    label = input("Enter data example (y): ")
    X.append(features)
    y.append(label)

Coords_ = list(map(float, input("Prediction, enter your input (x1,x2,x3 ...): ").split(",")))

min_distance = None
predicted_label = None

for i in range(len(X)):
    dist = euclidean_distance(Coords_, X[i])
    if dist is None:
        print("Error: Input and example must have the same size")
        exit()
    if min_distance is None or dist < min_distance:
        min_distance = dist
        predicted_label = y[i]
print(f"Min Euclidean distance: {min_distance:.2f}")
print(f"Result : {predicted_label}")