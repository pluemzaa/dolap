import math

X, y = [], []

while True:
    x_input = input("Enter data example (x1,x2,x3 ...): ").strip()
    if x_input.lower() == "exit":
        break
    y_input = input("Enter data example (y): ").strip()
    
    values = x_input.split(',')
    if all(v.replace('.', '', 1).isdigit() for v in values):
        X.append([float(v) for v in values])
        y.append(y_input)
    else:
        print("Invalid input, please enter numbers separated by commas.")

x_predict = input("Prediction, enter your input (x1,x2,x3 ...): ").strip()
predict_values = x_predict.split(',')
if not all(v.replace('.', '', 1).isdigit() for v in predict_values):
    print("Invalid prediction input.")
    exit()
x_predict_values = [float(v) for v in predict_values]

min_dist, min_label = None, None
for features, label in zip(X, y):
    if len(features) == len(x_predict_values):
        dist = math.sqrt(sum((a - b) ** 2 for a, b in zip(features, x_predict_values)))
        if min_dist is None or dist < min_dist:
            min_dist, min_label = dist, label

if min_dist is not None:
    print(f"Min Euclidean distance: {min_dist:.2f}")
    print(f"Result : {min_label}")
else:
    print("No valid comparison.")