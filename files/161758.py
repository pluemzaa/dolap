X = []
y = []

while True:
    x_input = input("Enter data example (x1,x2,x3 ...): ")
    if x_input.strip().lower() == "exit":
        break
    x_values = [float(i.strip()) for i in x_input.split(",")]
    label = input("Enter data example (y): ").strip()
    X.append(x_values)
    y.append(label)

test_input = input("Prediction, enter your input (x1,x2,x3 ...): ")
X_input = [float(i.strip()) for i in test_input.split(",")]

min_distance = None
predicted_label = None

for i in range(len(X)):
    if len(X[i]) != len(X_input):
        print("Error: Input size does not match with example at index", i)
        continue
    total = 0
    for j in range(len(X_input)):
        total += (X[i][j] - X_input[j]) ** 2
    distance = total ** 0.5
    if (min_distance is None) or (distance < min_distance):
        min_distance = distance
        predicted_label = y[i]

print(f"Min Euclidean distance: {min_distance:.2f}")
print(f"Result : {predicted_label}")