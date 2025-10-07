import math

X = []
y = []

while True:
    x_input = input("Enter data example (x1,x2,x3 ...): ")
    if x_input.lower() == "exit":
        break
    x_list = x_input.split(",")
    try:
        x_list = [float(i.strip()) for i in x_list]
    except:
        print("Invalid input. Try again.")
        continue
    X.append(x_list)
    y_label = input("Enter data example (y): ")
    y.append(y_label)

predict_input = input("Prediction, enter your input (x1,x2,x3 ...): ")
try:
    p = [float(i.strip()) for i in predict_input.split(",")]
except:
    print("Invalid input.")
    exit()

min_distance = None
min_index = -1

for i in range(len(X)):
    q = X[i]
    if len(p) != len(q):
        print("Length mismatch, skipping sample")
        continue

    sum_of_squares = 0
    for j in range(len(p)):
        diff = p[j] - q[j]
        sum_of_squares += diff ** 2

    distance = math.sqrt(sum_of_squares)
    if min_distance is None or distance < min_distance:
        min_distance = distance
        min_index = i

if min_index == -1:
    print("No valid sample to compare.")
else:
    print(f"Min Euclidean distance: {min_distance:.2f}")
    print("Result :", y[min_index])