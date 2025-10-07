print("ป้อนเวกเตอร์ตัวที่ 1 (จำนวน 3 ตัว):")
v1 = []
for i in range(3):
    num = float(input(f"สมาชิกตัวที่ {i+1}: "))
    v1.append(num)
print("ป้อนเวกเตอร์ตัวที่ 2 (จำนวน 3 ตัว):")
v2 = []
for i in range(3):
    num = float(input(f"สมาชิกตัวที่ {i+1}: "))
    v2.append(num)
dot_product = v1[0]*v2[0] + v1[1]*v2[1] + v1[2]*v2[2]
print(f"Dot product คือ: {dot_product}")