import math

def euclidean_distance(x1, x2):
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(x1, x2)))

X = []
y = []

while True:
    x_input = input("Enter data example (x1,x2,x3 ...): ")
    if x_input.lower() == "exit":
        break
    try:
        x_list = list(map(float, x_input.split(",")))
    except ValueError:
        print("Invalid input format. Please enter numbers separated by commas.")
        continue
    label = input("Enter data example (y): ")
    X.append(x_list)
    y.append(label)

x_pred_input = input("Prediction, enter your input (x1,x2,x3 ...): ")
try:
    x_pred = list(map(float, x_pred_input.split(",")))
except ValueError:
    print("Invalid input format.")
    exit()

min_dist = float("inf")
min_index = -1

for i, x_example in enumerate(X):
    if len(x_example) != len(x_pred):
        print(f"Warning: Skipping example #{i+1} due to dimension mismatch.")
        continue
    dist = euclidean_distance(x_pred, x_example)
    if dist < min_dist:
        min_dist = dist
        min_index = i

if min_index == -1:
    print("No matching dimensional data found.")
else:
    print(f"Min Euclidean distance: {min_dist:.2f}")
    print(f"Result : {y[min_index]}")