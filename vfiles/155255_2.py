x1 = float(input("Enter the x-coordinate of point 1: "))
y1 = float(input("Enter the y-coordinate of point 1: "))

# รับค่าพิกัดของจุดที่ 2
x2 = float(input("Enter the x-coordinate of point 2: "))
y2 = float(input("Enter the y-coordinate of point 2: "))

# คำนวณหาระยะห่างระหว่างจุด
distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# แสดงผลลัพธ์โดยให้แสดงทศนิยม 2 ตำแหน่ง