X = []
y = []


while True:
    x_str = input("Enter data example (x1,x2,x3 ...): ")
    if x_str.lower() == "exit":
        break
    label = input("Enter data example (y): ")
    X.append([float(v) for v in x_str.split(",")])
    y.append(label)


x_input = [float(v) for v in input("Prediction, enter your input (x1,x2,x3 ...): ").split(",")]


min_index = min(
    range(len(X)),
    key=lambda i: sum((a - b) ** 2 for a, b in zip(X[i], x_input)) ** 0.5
)


min_distance = sum((a - b) ** 2 for a, b in zip(X[min_index], x_input)) ** 0.5
print(f"Min Euclidean distance: {min_distance:.2f}")
print(f"Result : {y[min_index]}")