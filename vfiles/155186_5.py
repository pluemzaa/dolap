# โปรแกรมปรับข้อมูลให้อยู่ในช่วง 0 ถึง 1 ด้วย Min-Max Normalization

# รับข้อมูลจากผู้ใช้ โดยคั่นด้วยเครื่องหมายคอมมา
data = input("กรอกตัวเลขจำนวน 5 จำนวน คั่นด้วย ,: ")
numbers = [int(x) for x in data.split(",")]

# หาค่าน้อยที่สุดและมากที่สุด
min_val = min(numbers)
max_val = max(numbers)

# คำนวณค่านอร์มัลไลซ์ (normalized) สำหรับแต่ละตัว
normalized = [(x - min_val) / (max_val - min_val) for x in numbers]

# แสดงผลลัพธ์
print("Normalized values:")
for n in normalized:
    print("%.2f" % n)