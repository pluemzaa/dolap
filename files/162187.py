import math


X = []
y = []


while True:
    x_input = input("Enter data example (x1,x2,x3 ...): ")
    if x_input.lower() == "exit":
        break
    x = [float(i.strip()) for i in x_input.split(",")]
    label = input("Enter data example (y): ")
    X.append(x)
    y.append(label)


predict_input = input("Prediction, enter your input (x1,x2,x3 ...): ")
predict = [float(i.strip()) for i in predict_input.split(",")]


min_dist = None
result = None

for i in range(len(X)):
    dist = math.sqrt(sum((X[i][j] - predict[j]) ** 2 for j in range(len(predict))))
    if min_dist is None or dist < min_dist:
        min_dist = dist
        result = y[i]


print(f"Min Euclidean distance: {min_dist:.2f}")
print(f"Result : {result}")