import math

# ฟังก์ชันคำนวณ Euclidean distance
def euclidean_distance(a, b):
    sum_sq = 0
    for i in range(len(a)):
        sum_sq += (a[i] - b[i]) ** 2
    return math.sqrt(sum_sq)

# เก็บข้อมูลตัวอย่าง
X = []
y = []

# รับข้อมูลตัวอย่างจากผู้ใช้
while True:
    x_input = input("Enter data example (x1,x2,x3 ...): ")
    if x_input.lower() == "exit":
        break
    x_values = list(map(float, x_input.split(",")))
    label = input("Enter data example (y): ")
    X.append(x_values)
    y.append(label)

# รับข้อมูลที่ต้องการทำนาย
X_input = list(map(float, input("Prediction, enter your input (x1,x2,x3 ...): ").split(",")))

# ตรวจสอบว่ามีข้อมูลตัวอย่างหรือไม่
if not X:
    print("No data examples to compare.")
else:
    min_dist = None
    min_label = None

    # วนหาข้อมูลตัวอย่างที่มีระยะทางน้อยที่สุด
    for i in range(len(X)):
        if len(X[i]) != len(X_input):
            print("Error: Input size does not match example data size.")
            exit()
        dist = euclidean_distance(X_input, X[i])
        if min_dist is None or dist < min_dist:
            min_dist = dist
            min_label = y[i]

    # แสดงผลลัพธ์
    print(f"Min Euclidean distance: {min_dist:.2f}")
    print(f"Result : {min_label}")