# ข้อความสัตว์จากผู้ใช้
animal_text = input("Enter your pets: ")  # เช่น Dog,Cat,Dog,Fish,Cat

# ใช้ split แยกข้อความเป็น list
animals = animal_text.split(',')

# แสดงผลลัพธ์ของ split แบบในสไลด์
print(animals)
print(len(animals))

# สร้าง dictionary สำหรับรหัสสัตว์
code = {
    "Dog": 0,
    "Cat": 1,
    "Fish": 2
}

# เตรียม list สำหรับเก็บรหัส
codes = []

# วนลูปแปลงชื่อสัตว์ → รหัส
for a in animals:
    c = code[a]
    codes.append(str(c))

# แสดงผลลัพธ์สุดท้าย
print("Code of your pets:", ",".join(codes))