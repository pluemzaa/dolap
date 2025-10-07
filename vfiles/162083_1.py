import math

# ลิสต์สำหรับเก็บข้อมูลตัวอย่าง (features) และ label
X = []
y = []

# 1. รับข้อมูลตัวอย่าง
while True:
    x_input = input("Enter data example (x1,x2,x3 ...): ")
    if x_input.lower() == 'exit':
        break
    try:
        x_vector = [float(i.strip()) for i in x_input.split(",")]
    except ValueError:
        print("Invalid input. Please enter only numbers.")
        continue

    label = input("Enter data example (y): ")
    X.append(x_vector)
    y.append(label)

# ถ้าไม่มีข้อมูลเลย ก็หยุดการทำงาน
if not X:
    print("No data provided. Exiting...")
    exit()

# 2. รับข้อมูลสำหรับทำนาย
x_predict_input = input("Prediction, enter your input (x1,x2,x3 ...): ")
try:
    x_predict = [float(i.strip()) for i in x_predict_input.split(",")]
except ValueError:
    print("Invalid input. Please enter only numbers.")
    exit()

# ตรวจสอบว่าขนาดข้อมูลเข้ากันได้กับข้อมูลตัวอย่าง
if any(len(x) != len(x_predict) for x in X):
    print("Error: All vectors must have the same size as the input.")
    exit()

# 3. คำนวณ Euclidean distance และหาค่าที่น้อยที่สุด
min_distance = None
predicted_label = None

for i in range(len(X)):
    distance = math.sqrt(sum((X[i][j] - x_predict[j]) ** 2 for j in range(len(x_predict))))
    if (min_distance is None) or (distance < min_distance):
        min_distance = distance
        predicted_label = y[i]

# 4. แสดงผลลัพธ์
print(f"Min Euclidean distance: {min_distance:.2f}")
print(f"Result : {predicted_label}")