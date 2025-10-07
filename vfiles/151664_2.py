# 1. สร้าง Dictionary เพื่อเก็บข้อมูลรหัสของสัตว์เลี้ยง
#    - Key คือชื่อสัตว์ (string)
#    - Value คือรหัส (integer)
pet_code_map = {
    "Dog": 0,
    "Cat": 1,
    "Fish": 2
    # สามารถเพิ่มสัตว์เลี้ยงชนิดอื่นๆ และรหัสที่นี่ได้
}

# 2. รับข้อมูลจากผู้ใช้เป็นข้อความหนึ่งบรรทัด
#    ตัวอย่าง: Dog,Cat,Dog,Fish,Cat
input_string = input("กรุณาป้อนชื่อสัตว์เลี้ยงโดยคั่นด้วยเครื่องหมายคอมม่า (เช่น Dog,Cat,Fish): ")

# 3. แยกข้อความที่รับมาให้กลายเป็น List ของชื่อสัตว์
#    ใช้ฟังก์ชัน .split(',') เพื่อตัดข้อความตรงเครื่องหมายคอมม่า
pet_name_list = input_string.split(',')

# 4. วนลูปเพื่อแปลงชื่อสัตว์เป็นรหัสตัวเลข
#    - สร้าง List ว่างชื่อ result_codes เพื่อรอเก็บผลลัพธ์
#    - วนลูปใน pet_name_list ทีละตัว
result_codes = []
for pet_name in pet_name_list:
    # นำชื่อสัตว์ที่ได้ (pet_name) ไปค้นหาใน pet_code_map เพื่อเอารหัสออกมา
    code = pet_code_map[pet_name]
    # นำรหัสที่ได้ (code) ไปเพิ่มใน List ของผลลัพธ์
    result_codes.append(code)

# 5. จัดรูปแบบผลลัพธ์เพื่อแสดงผล
#    - result_codes ตอนนี้จะเป็น List ของตัวเลข เช่น [0, 1, 0, 2, 1]
#    - เราต้องแปลงตัวเลขแต่ละตัวให้เป็น string ก่อน
#    - จากนั้นใช้ .join(',') เพื่อรวม List ของ string ให้กลายเป็นข้อความเดียวโดยมีคอมม่าคั่น
#      วิธีเขียนแบบ List Comprehension (กระชับและนิยมใช้ใน Python)
output_string = ",".join([str(code) for code in result_codes])

# 6. แสดงผลลัพธ์สุดท้าย
print(f"ข้อมูลที่รับมา: {input_string}")
print(f"รหัสที่แปลงได้คือ: {output_string}")