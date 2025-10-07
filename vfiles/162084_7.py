import math

X = []
y = []

while True:
    x_input = input("Enter data example (x1,x2,x3 ...): ")
    if x_input.lower() == "exit":
        break
    features = list(map(float, x_input.split(",")))
    label = input("Enter data example (y): ")
    X.append(features)
    y.append(label)

pred_input = input("Prediction, enter your input (x1,x2,x3 ...): ")
pred_features = list(map(float, pred_input.split(",")))

min_distance = None
predicted_label = None

for features, label in zip(X, y):
   
    if len(features) != len(pred_features):
        print("Feature length mismatch! Skipping this example.")
        continue
  
    distance = math.sqrt(sum((a - b) ** 2 for a, b in zip(features, pred_features)))
    if min_distance is None or distance < min_distance:
        min_distance = distance
        predicted_label = label

if min_distance is not None:
    print(f"Min Euclidean distance: {min_distance:.2f}")
    print(f"Result : {predicted_label}")
else:
    print("No valid examples for comparison.")