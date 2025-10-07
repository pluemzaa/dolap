import math

def parse_vector(s):
    return [float(x.strip()) for x in s.split(',') if x.strip() != '']

X = []
y = []

while True:
    x_str = input("Enter data example (x1,x2,x3 ...): ")
    if x_str.strip().lower() == "exit":
        break
    try:
        x_vec = parse_vector(x_str)
    except ValueError:
        print("Error: invalid feature values")
        continue
    label = input("Enter data example (y): ")
    X.append(x_vec)
    y.append(label)

if len(X) == 0:
    print("Error: no training data")
else:
    x_input_str = input("Prediction, enter your input (x1,x2,x3 ...): ")
    try:
        x_input = parse_vector(x_input_str)
    except ValueError:
        print("Error: invalid feature values")
        x_input = None

    if x_input is not None:
        min_dist = None
        min_label = None
        mismatch = False

        for xi, yi in zip(X, y):
            if len(xi) != len(x_input):
                print("Error: Vectors must have the same size")
                mismatch = True
                break

            sum_sq = 0.0
            for a, b in zip(xi, x_input):
                diff = a - b
                sum_sq += diff * diff
            d = math.sqrt(sum_sq)

            if (min_dist is None) or (d < min_dist):
                min_dist = d
                min_label = yi

        if not mismatch:
            print(f"Min Euclidean distance: {min_dist:.2f}")
            print(f"Result : {min_label}")