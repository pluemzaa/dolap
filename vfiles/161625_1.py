import math

# --- ส่วนรับข้อมูล ---
data = []
label = []
while True:
    nums_input = input('Enter data example (x1,x2,x3 ...): ')
    if nums_input.lower() == 'exit':
        break
    
    nums = [float(x) for x in nums_input.split(',')]
    data.append(nums)
    
    lab = input('Enter data example (y): ')
    label.append(lab)

# --- ส่วนทำนาย ---
feat_input = input('Prediction, enter your input (x1,x2,x3 ...): ')
feat = [float(x) for x in feat_input.split(',')]

min_distance = float('inf')
prediction_result = None

# วนลูปเพื่อหาค่าระยะทางที่น้อยที่สุด
for i in range(len(data)):
    # คำนวณ Euclidean Distance
    sum_of_squares = 0
    for j in range(len(data[i])):
        difference = data[i][j] - feat[j]
        sum_of_squares += difference ** 2
    
    distance = math.sqrt(sum_of_squares)
    
    # เปรียบเทียบเพื่อหาค่าน้อยที่สุด
    if distance < min_distance:
        min_distance = distance
        prediction_result = label[i]

# แสดงผลลัพธ์
print(f"Min Euclidean distance: {min_distance:.2f}")
print(f"Result : {prediction_result}")