x = []
y = []

while True:
    data = input("Enter data example (x1,x2,x3 ...): ")
    if data == "exit":
        break
    label = input("Enter data example (y): ")
    features = [float(z) for z in data.split(",")]
    x.append(features)
    y.append(label)

tr = [float(z) for z in input("Prediction, enter your input (x1,x2,x3 ...): ").split(",")]

min_dist = float("inf")
result = None

for xi, yi in zip(x, y):
    dist = sum((a - b) ** 2 for a, b in zip(xi, tr)) ** 0.5
    if dist < min_dist:
        min_dist = dist
        result = yi

print("Min Euclidean distance:", round(min_dist, 2))
print("Result:", result)