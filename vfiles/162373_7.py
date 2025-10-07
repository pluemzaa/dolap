import math

def euclidean_distance(point1, point2):
    """
    ฟังก์ชันสำหรับคำนวณระยะห่างแบบยูคลิดระหว่างจุด 2 จุด
    """
    # ตรวจสอบให้แน่ใจว่าจำนวนมิติตรงกัน
    if len(point1) != len(point2):
        # คืนค่าระยะทางเป็นอนันต์เพื่อให้ไม่ถูกเลือก
        return float('inf')
        
    distance_squared = 0
    for i in range(len(point1)):
        distance_squared += (point1[i] - point2[i]) ** 2
    return math.sqrt(distance_squared)

# สร้างลิสต์เปล่าเพื่อเก็บข้อมูลตัวอย่าง
X_train = []
y_train = []

# --- 1. ส่วนของการรับข้อมูลตัวอย่าง ---
while True:
    features_input = input("Enter data example (x1,x2,x3 ...) or exit: ")

    if features_input.lower() == 'exit':
        break

    try:
        # * จุดที่แก้ไข *
        # แทนที่ '.' ด้วย ' ' เพื่อให้รองรับ input ทั้งสองแบบ แล้วจึง split
        cleaned_input = features_input.replace('.', ' ')
        features = [float(val) for val in cleaned_input.split()]
        
        label = input("Enter data example (y): ")

        X_train.append(features)
        y_train.append(label)

    except ValueError:
        print("Invalid input. Please enter numbers separated by spaces or dots.")
        continue

# --- 2. ส่วนของการทำนายผล ---
if not X_train:
    print("No sample data entered. The program will now exit.")
else:
    try:
        predict_input_str = input("Prediction, enter your input (x1,x2,x3 ...): ")
        
        # * จุดที่แก้ไข (ใช้หลักการเดียวกัน) *
        cleaned_predict_input = predict_input_str.replace('.', ' ')
        predict_point = [float(val) for val in cleaned_predict_input.split()]
        
        min_distance = float('inf')
        predicted_label = None

        # --- 3. วนลูปเพื่อหาข้อมูลที่ใกล้ที่สุด ---
        for i, sample_point in enumerate(X_train):
            distance = euclidean_distance(predict_point, sample_point)
            
            if distance < min_distance:
                min_distance = distance
                predicted_label = y_train[i]

        # --- 4. แสดงผลลัพธ์ ---
        if predicted_label is None:
            print("Could not make a prediction. Check input dimensions.")
        else:
            print(f"Min Euclidean distance: {min_distance:.2f}")
            print(f"Result: {predicted_label}")

    except ValueError:
        print("Invalid prediction input. Please enter numbers separated by spaces or dots.")
    except Exception as e:
        print(f"An error occurred: {e}")