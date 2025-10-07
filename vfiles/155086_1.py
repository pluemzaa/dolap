import math

x1 = int(input("Enter x1: "))
y1 = int(input("Enter y1: "))
x2 = int(input("Enter x2: "))
y2 = int(input("Enter y2: "))

# คำนวณระยะทางระหว่างสองจุด
d = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# แสดงผลแบบ %.2f เหมือนในสไลด์
print('distance = %.2f' % d)