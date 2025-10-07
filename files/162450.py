import math

def calculate_euclidean_distance(p, q):
    if len(p) != len(q):
        raise ValueError("Vectors must have the same size")
    sum_of_squares = sum((pi - qi) ** 2 for pi, qi in zip(p, q))
    return math.sqrt(sum_of_squares)

X = []
y = []

while True:
    data_str = input("Enter data example (x1,x2,x3 ...): ")
    if data_str.lower() == "exit":
        break

    try:
        features = [float(coord) for coord in data_str.split(",")]
    except ValueError:
        print("Error: Invalid input. Please enter numbers separated by commas.")
        continue

    label = input("Enter data example (y): ")
    X.append(features)
    y.append(label)

X_input_str = input("Prediction, enter your input (x1,x2,x3 ...): ")
X_input = [float(coord) for coord in X_input_str.split(",")]

distances = []
for features in X:
    distance = calculate_euclidean_distance(X_input, features)
    distances.append(distance)

min_distance = min(distances)
min_index = distances.index(min_distance)

print(f"Min Euclidean distance: {min_distance:.2f}")
print(f"Prediction: {y[min_index]}")