import math

def euclidean_distance(p_list, q_list):
    if len(p_list) != len(q_list):
        return None  # ขนาดไม่เท่ากัน
    sum_sq = 0
    for i in range(len(p_list)):
        diff = p_list[i] - q_list[i]
        sum_sq += diff ** 2
    return math.sqrt(sum_sq)

# 1. รับข้อมูลตัวอย่างจนพิมพ์ exit
X = []
y = []

while True:
    data_x = input("Enter data example (x1,x2,x3 ...): ")
    if data_x.lower() == "exit":
        break
    data_y = input("Enter data example (y): ")
    
    # แปลงข้อมูล x เป็น list ของ float
    try:
        x_values = [float(v) for v in data_x.split(",")]
    except:
        print("Invalid input for features, try again.")
        continue
    
    X.append(x_values)
    y.append(data_y)

# 2. รับข้อมูลที่ต้องการทำนาย
input_x = input("Prediction, enter your input (x1,x2,x3 ...): ")
try:
    input_values = [float(v) for v in input_x.split(",")]
except:
    print("Invalid input for prediction features.")
    exit()

# 3. หาค่าระยะ Euclidean ที่น้อยที่สุด
min_dist = None
min_index = -1

for i, x_example in enumerate(X):
    dist = euclidean_distance(input_values, x_example)
    if dist is None:
        print(f"Error: Input size does not match example at index {i}")
        exit()
    if (min_dist is None) or (dist < min_dist):
        min_dist = dist
        min_index = i

# แสดงผลลัพธ์
print(f"Min Euclidean distance: {min_dist:.2f}")
print(f"Result : {y[min_index]}")