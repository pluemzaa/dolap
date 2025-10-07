# โปรแกรมปรับช่วงข้อมูลให้อยู่ระหว่าง 0 ถึง 1 (Min-Max Normalization)

# รับข้อมูลจากผู้ใช้ คั่นด้วย comma แล้วแปลงเป็น int
data = input("Enter a series of numbers separated by commas: ")
x = [int(i) for i in data.split(",")]

# หาค่าต่ำสุดและค่าสูงสุด
min_val = min(x)
max_val = max(x)

# คำนวณค่า normalized ทีละตัวในลิสต์
x_scaled = [(i - min_val) / (max_val - min_val) for i in x]

# แสดงผลลัพธ์
print("Normalized values:")
for val in x_scaled:
    print("%.2f" % val)