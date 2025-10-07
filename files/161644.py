import math

X = []
y = []

while True:
    data_input = input("Enter data example (x1,x2,x3 ...): ")
    if data_input.lower() == "exit":
        break
    label_input = input("Enter data example (y): ")
    X.append(list(map(float, data_input.split(","))))
    y.append(label_input)

X_input = list(map(float, input("Prediction, enter your input (x1,x2,x3 ...): ").split(",")))

for sample in X:
    if len(sample) != len(X_input):
        print("Error: Vectors must have the same size")
        exit()

min_distance = None
min_label = None
for sample, label in zip(X, y):
    total = sum((xi - si) ** 2 for xi, si in zip(X_input, sample))
    distance = math.sqrt(total)
    if min_distance is None or distance < min_distance:
        min_distance = distance
        min_label = label

print(f"Min Euclidean distance: {min_distance:.2f}")
print(f"Result : {min_label}")