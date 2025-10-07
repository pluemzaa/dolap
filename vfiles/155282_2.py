import math


x1 = float(input("ป้อนค่าx1: "))
y1 = float(input("ป้อนค่า y1: "))
x2 = float(input("ป้อนค่า x2: "))
y2 = float(input("ป้อนค่า y2: "))
distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print("ระยะห่างระหว่างสองจุดคือ:", distance)