import math

X = []  # list ของ features
Y = []  # list ของ labels

# รับข้อมูลตัวอย่าง
while True:
    data = input("Enter data example (x1,x2,x3,...): ")
    if data.lower() == "exit":
        break
    features = list(map(float, data.split(",")))
    label = input("Enter data example (y): ")
    X.append(features)
    Y.append(label)

# รับข้อมูลที่จะทำนาย
X_input = list(map(float, input("Prediction, enter your input (x1,x2,x3,...): ").split(",")))

# คำนวณ Euclidean distance และหาค่าน้อยที่สุด
min_distance = None
predicted_label = None

for i in range(len(X)):
    dist = math.sqrt(sum((X_input[j] - X[i][j]) ** 2 for j in range(len(X[i]))))
    if min_distance is None or dist < min_distance:
        min_distance = dist
        predicted_label = Y[i]

# แสดงผลตามรูปแบบโจทย์
print(f"Min Euclidean distance: {min_distance:.2f}")
print(f"Result : {predicted_label}")