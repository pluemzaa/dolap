import math

def euclidean_distance(a, b):
    return math.sqrt(sum((x - y) ** 2 for x, y in zip(a, b)))

x = []
y = []
while True:
    xin = input("Enter data example (x1,x2,x3 ...): ")
    if xin.strip().lower() == 'exit':
        break
    xin_vals = [float(i) for i in xin.strip().split(',')]
    yin = input("Enter data example (y): ")
    x.append(xin_vals)
    y.append(yin.strip())

x_input_row = input("Prediction, enter your input (x1,x2,x3 ...): ")
x_input = [float(i) for i in x_input_row.strip().split(',')]

min_dist = None
min_index = -1

for idx, sample in enumerate(x):
    if len(sample) != len(x_input):
        print(f"Warning: ค่าของแถวที่ {idx+1} ไม่เท่ากับข้อมูลที่ใช้ในการ input!")
        continue
    
    dist = euclidean_distance(sample, x_input)
    if (min_dist is None) or (dist < min_dist):
        min_dist = dist
        min_index = idx
        
if min_index == -1:
    print("ไม่พบข้อมูลที่จะใช้ในการคำนวณได้")
else:
    print(f"Min Euclidean distance: {min_dist:.2f}")
    print(f"Result : {y[min_index]}")