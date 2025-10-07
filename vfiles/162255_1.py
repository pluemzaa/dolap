import math
x = []
y = []

while True:
    x_input = input("Enter data example (x1,x2,x3 ...): ")
    if x_input.split().lower() == "exit":
        break
    x_values = [float(v.strip()) for v in x_input.split(",")]
    lable = input("Enter data example (y): ")
    x.append(x_values)
    y.append(lable)
    
X_input = [float(v.strip()) for v in input("Prediction, enter your input (x1,x2,x3 ...): ")]
min_distance = None
prediction_lable = None

for i in range(len(x)):
    distance = math.sqrt(sum((x_input[j] - x[i][j]))**2 for j in range(len(x_input)))
    if min_distance is None or distance < min_distance:
        min_distance = distance
        prediction_lable = y[i]
        
print(f"Min Euclidean distance: {min_distance:.2f}")
print(f"Result : {prediction_lable}")