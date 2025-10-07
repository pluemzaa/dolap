import math

# รับค่าจากผู้ใช้
x1 = float(input("ป้อนค่า x1: "))
y1 = float(input("ป้อนค่า y1: "))
x2 = float(input("ป้อนค่า x2: "))
y2 = float(input("ป้อนค่า y2: "))

# คำนวณระยะทาง
distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# แสดงผลลัพธ์
print("ระยะห่างระหว่างสองจุดคือ:", distance)