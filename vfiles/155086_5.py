import math

# รับค่าจากผู้ใช
x1 = float(input("Enter the x-coordinate of point 1: "))
y1 = float(input("Enter the y-coordinate of point 1: "))
x2 = float(input("Enter the x-coordinate of point 2: "))
y2 = float(input("Enter the y-coordinate of point 2: "))

# คำนวณระยะทาง
distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# แสดงผลลัพธ์ทศนิยม 2 ตำแหน่ง
print(f"The distance between the two points is: {distance:.2f}")