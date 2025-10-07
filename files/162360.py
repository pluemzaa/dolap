import math

# ฟังก์ชันคำนวณ Euclidean distance
def euclidean_distance(p, q):
    if len(p) != len(q):
        return None
    sum_sq = 0
    for i in range(len(p)):
        sum_sq += (p[i] - q[i]) ** 2
    return math.sqrt(sum_sq)

# เก็บข้อมูลตัวอย่าง
X = []  # เก็บ feature
y = []  # เก็บ label

# รับข้อมูลตัวอย่างจากผู้ใช้
while True:
    x_input = input("Enter data example (x1,x2,x3 ...): ")
    if x_input.lower() == "exit":
        break
    x_list = [float(val) for val in x_input.split(",")]
    label = input("Enter data example (y): ")
    X.append(x_list)
    y.append(label)

# รับข้อมูลที่จะทำนาย
X_input = [float(val) for val in input("Prediction, enter your input (x1,x2,x3 ...): ").split(",")]

# หาข้อมูลตัวอย่างที่มี Euclidean distance น้อยที่สุด
min_distance = None
predicted_label = None

for i in range(len(X)):
    dist = euclidean_distance(X_input, X[i])
    if min_distance is None or dist < min_distance:
        min_distance = dist
        predicted_label = y[i]

# แสดงผลลัพธ์
if min_distance is not None:
    print(f"Min Euclidean distance: {min_distance:.2f}")
    print(f"Result : {predicted_label}")
else:
    print("No data to compare.")