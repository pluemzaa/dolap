import math

def euclidean_distance(point1, point2):
    """
    ฟังก์ชันสำหรับคำนวณระยะห่างแบบยูคลิดระหว่างจุด 2 จุด (ในรูปแบบ list)
    """
    distance_squared = 0
    # คำนวณผลรวมของ (p1[i] - p2[i])^2
    for i in range(len(point1)):
        distance_squared += (point1[i] - point2[i]) ** 2
    return math.sqrt(distance_squared)

# สร้างลิสต์เปล่าเพื่อเก็บข้อมูลตัวอย่าง
X_train = []
y_train = []

# --- 1. ส่วนของการรับข้อมูลตัวอย่าง ---
while True:
    # รับข้อมูล features (x1,x2,x3 ...)
    features_input = input("Enter data example (x1,x2,x3 ...) or exit: ")

    # หากผู้ใช้พิมพ์ 'exit' ให้ออกจากลูป
    if features_input.lower() == 'exit':
        break

    try:
        # แปลง input (ที่คั่นด้วย space) ให้เป็น list ของตัวเลข float
        features = [float(val) for val in features_input.split()]
        
        # รับข้อมูล label (y)
        label = input("Enter data example (y): ")

        # เพิ่มข้อมูล vàoในลิสต์ตัวอย่าง
        X_train.append(features)
        y_train.append(label)

    except ValueError:
        print("Invalid input. Please enter numbers separated by spaces.")
        continue

# --- 2. ส่วนของการทำนายผล ---
# ตรวจสอบว่ามีข้อมูลตัวอย่างหรือไม่
if not X_train:
    print("No sample data entered. The program will now exit.")
else:
    try:
        # รับข้อมูลที่ต้องการทำนาย
        predict_input_str = input("Prediction, enter your input (x1,x2,x3 ...): ")
        predict_point = [float(val) for val in predict_input_str.split()]

        # ตรวจสอบว่าจำนวนมิติของข้อมูลตรงกันหรือไม่
        if len(predict_point) != len(X_train[0]):
             print(f"Error: Input must have {len(X_train[0])} dimensions, matching the sample data.")
        else:
            min_distance = float('inf')
            predicted_label = None

            # --- 3. วนลูปเพื่อหาข้อมูลที่ใกล้ที่สุด ---
            for i, sample_point in enumerate(X_train):
                # คำนวณระยะห่าง
                distance = euclidean_distance(predict_point, sample_point)
                
                # หากระยะทางที่คำนวณได้น้อยกว่าค่าต่ำสุดที่เคยเจอ ให้ทำการอัปเดต
                if distance < min_distance:
                    min_distance = distance
                    predicted_label = y_train[i]

            # --- 4. แสดงผลลัพธ์ ---
            print(f"Min Euclidean distance: {min_distance:.2f}")
            print(f"Result: {predicted_label}")

    except ValueError:
        print("Invalid prediction input. Please enter numbers separated by spaces.")
    except Exception as e:
        print(f"An error occurred: {e}")