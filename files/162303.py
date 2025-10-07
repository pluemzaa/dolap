import math 
X = []  # features
y = []  # labels
while True:
    data = input("Enter data example (x1,x2,x3 ...): ")
    if data.lower() == "exit":  # ถ้าพิมพ์ exit ให้หยุดรับข้อมูล
        break
    parts = data.split(",")   
    features = []
    for p in parts:
        features.append(float(p)) 
    label = input("Enter data example (y): ")  
    X.append(features)  
    y.append(label)     
input_data = input("Prediction, enter your input (x1,x2,x3 ...): ")
parts = input_data.split(",")
X_input = []
for p in parts:
    X_input.append(float(p))
min_distance = float("inf") 
predicted_label = None
for i in range(len(X)):  
    total = 0
    for j in range(len(X_input)):  
        total += (X_input[j] - X[i][j]) ** 2  
    distance = math.sqrt(total)  # ถอดรากที่สอง
    if distance < min_distance:
        min_distance = distance
        predicted_label = y[i]
print(f"Min Euclidean distance: {min_distance:.2f}")
print(f"Result : {predicted_label}")