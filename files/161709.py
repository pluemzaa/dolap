import math

# ฟังก์ชันคำนวณ Euclidean distance
def euclidean_distance(p, q):
    return math.sqrt(sum((pi - qi) ** 2 for pi, qi in zip(p, q)))

# เก็บข้อมูลตัวอย่าง
X = []
y = []

# รับข้อมูลตัวอย่าง
while True:
    x_input = input("Enter data example (x1,x2,x3 ...): ")
    if x_input.lower() == "exit":
        break
    x_values = list(map(float, x_input.split(',')))
    label = input("Enter data example (y): ")
    X.append(x_values)
    y.append(label)

# รับข้อมูลที่ต้องการทำนาย
test_input = input("Prediction, enter your input (x1,x2,x3 ...): ")
test_vector = list(map(float, test_input.split(',')))

# คำนวณ Euclidean distance กับทุกตัวอย่าง
min_distance = float('inf')
predicted_label = None

for i in range(len(X)):
    dist = euclidean_distance(test_vector, X[i])
    if dist < min_distance:
        min_distance = dist
        predicted_label = y[i]

# แสดงผล
print(f"Min Euclidean distance: {min_distance:.2f}")
print(f"Result : {predicted_label}")