import math
def euclidean_distance(p, q):   
    if len(p) != len(q):
        raise ValueError("Vectors must have the same size")   
    sum_of_squares = sum((a - b) ** 2 for a, b in zip(p, q))    
    return math.sqrt(sum_of_squares)
X = [] 
y = [] 
while True:    
    x_str = input("Enter data example (x1,x2,x3 ...): ")  
    if x_str.strip().lower() == "exit":
        break 
    x_vals = list(map(float, x_str.split(",")))
    label = input("Enter data example (y): ")
    X.append(x_vals)
    y.append(label)
x_input_str = input("Prediction, enter your input (x1,x2,x3 ...): ")
X_input = list(map(float, x_input_str.split(",")))
min_distance = None
predicted_label = None
for features, label in zip(X, y):
    distance = euclidean_distance(features, X_input)
    if min_distance is None or distance < min_distance:
        min_distance = distance
        predicted_label = label

print(f"Min Euclidean distance: {min_distance:.2f}")
print(f"Result : {predicted_label}")