import math
X = []
y = []

while True:
    x_str = input("Enter data example (x1,x2,x3 ...): ")
    if x_str.strip().lower() == "exit":
        break
    try:
        features = [float(v.strip()) for v in x_str.split(",")]
    except ValueError:
        print("Error: Please enter numbers separated by commas")
        continue
    
    label = input("Enter data example (y): ")
    X.append(features)
    y.append(label)

X_input_str = input("Prediction, enter your input (x1,x2,x3 ...): ")
try:
    X_input = [float(v.strip()) for v in X_input_str.split(",")]
except ValueError:
    print("Error: Please enter numbers separated by commas")
    exit()

if any(len(features) != len(X_input) for features in X):
    print("Error: Feature size mismatch between input and examples")
    exit()
min_dist = None
predicted_label = None

for features, label in zip(X, y):
    dist_sq = 0
    for a, b in zip(features, X_input):
        dist_sq += (a - b) ** 2
    dist = math.sqrt(dist_sq)

    if (min_dist is None) or (dist < min_dist):
        min_dist = dist
        predicted_label = label
print(f"Min Euclidean distance: {min_dist:.2f}")
print(f"Result : {predicted_label}")