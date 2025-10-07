import math


def euclidean_distance(a, b):
    return math.sqrt(sum((x - y) ** 2 for x, y in zip(a, b)))


X = []
y = []
while True:
    xin = input("Enter data example (x1,x2,x3 ...): ")
    if xin.strip().lower() == 'exit':
        break
    
    xin_vals = [float(i) for i in xin.strip().split(',')]
    yin = input("Enter data example (y): ")
    X.append(xin_vals)
    y.append(yin.strip())


X_input_raw = input("Prediction, enter your input (x1,x2,x3 ...): ")
X_input = [float(i) for i in X_input_raw.strip().split(',')]


min_dist = None
min_index = -1

for idx, sample in enumerate(X):
    
    if len(sample) != len(X_input):
        print(f"Warning: ตัวอย่างที่ {idx+1} รูปแบบข้อมูลไม่ตรงกับ input!")
        continue

    dist = euclidean_distance(sample, X_input)
    if (min_dist is None) or (dist < min_dist):
        min_dist = dist
        min_index = idx


if min_index == -1:
    print("ไม่พบข้อมูลตัวอย่างที่ใช้เปรียบเทียบได้")
else:
    
    print(f"Min Euclidean distance: {min_dist:.2f}")
    print(f"Result : {y[min_index]}")