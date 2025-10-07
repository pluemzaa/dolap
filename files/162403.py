X = []
y = []

while True:
    feature_input = input("Enter data example (x1,x2,x3 ...): ")
    if feature_input.lower() == "exit":
        break
    label_input = input("Enter data example (y): ")

    feature_vector = [float(x) for x in feature_input.split(",")]

    X.append(feature_vector)
    y.append(label_input)

X_input_str = input("Prediction, enter your input (x1,x2,x3 ...): ")
X_input = [float(x) for x in X_input_str.split(",")]

if any(len(vec) != len(X_input) for vec in X):
    print("Error: All vectors must have the same size")
else:
    min_distance = float('inf')
    min_index = -1

    for i in range(len(X)):
        sum_sq = 0
        for j in range(len(X[i])):
            diff = X[i][j] - X_input[j]
            sum_sq += diff ** 2
        distance = sum_sq ** 0.5

        if distance < min_distance:
            min_distance = distance
            min_index = i

    print(f"Min Euclidean distance: {min_distance:.2f}")
    print(f"Result : {y[min_index]}")