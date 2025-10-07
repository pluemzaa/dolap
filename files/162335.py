import math

X = []
y = []

while True:
    x_input = input("Enter data example (x1,x2,x3 ...): ")
    if x_input.lower() == "exit":
        break
    y_input = input("Enter data example (y): ")
    
    x_list = [float(i) for i in x_input.split(",")]
    
    X.append(x_list)
    y.append(y_input)

pred_input = input("Prediction, enter your input (x1,x2,x3 ...): ")
pred_data = [float(i) for i in pred_input.split(",")]

min_dist = None
pred_class = None

for i, sample in enumerate(X):
    dist = math.sqrt(sum((sample[j] - pred_data[j]) ** 2 for j in range(len(sample))))
    
    if (min_dist is None) or (dist < min_dist):
        min_dist = dist
        pred_class = y[i]

print(f"Min Euclidean distance: {min_dist:.2f}")
print(f"Result : {pred_class}")