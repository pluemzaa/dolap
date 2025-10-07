import math

# เก็บข้อมูลตัวอย่าง
X = []
y = []

# รับข้อมูลตัวอย่าง
while True:
    x_input = input("Enter data example (x1,x2,x3 ...): ")
    if x_input.lower() == "exit":
        break
    x_values = list(map(float, x_input.split(",")))
    label = input("Enter data example (y): ")
    X.append(x_values)
    y.append(label)

# รับข้อมูลที่ต้องการทำนาย
X_pred = list(map(float, input("Prediction, enter your input (x1,x2,x3 ...): ").split(",")))

# ฟังก์ชันคำนวณ Euclidean distance
def euclidean_distance(a, b):
    return math.sqrt(sum((ai - bi) ** 2 for ai, bi in zip(a, b)))

# คำนวณระยะทางกับทุกข้อมูลตัวอย่าง
distances = [euclidean_distance(X_pred, x_example) for x_example in X]

# หาตัวอย่างที่ใกล้ที่สุด
min_distance = min(distances)
min_index = distances.index(min_distance)
predicted_label = y[min_index]

# แสดงผล
print(f"Min Euclidean distance: {min_distance:.2f}")
print(f"Result : {predicted_label}")