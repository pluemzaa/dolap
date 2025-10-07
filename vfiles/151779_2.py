pet_name = {"Dog": 0, "Cat": 1, "Fish": 2}

# รับค่าจากผู้ใช้
pet_str = input("Enter your pets: ")

# แปลง input เป็น list ของชื่อสัตว์ (ลบช่องว่างและเปลี่ยนให้อักษรตัวแรกเป็นพิมพ์ใหญ่)
pets = [pet.strip().title() for pet in pet_str.split(',')]

# ตรวจสอบว่ามีสัตว์ครบ 5 ตัว
if len(pets) != 5:
    print("❌ Error: Please enter exactly 5 pet names.")
# ตรวจสอบว่าชื่อสัตว์แต่ละตัวอยู่ใน pet_name
elif not all(pet in pet_name for pet in pets):
    print("❌ Error: Invalid pet name. Please use only Dog, Cat, or Fish.")
else:
    # แปลงชื่อสัตว์เป็นรหัส
    codes = [pet_name[pet] for pet in pets]

    # แสดงผลลัพธ์ตามที่ต้องการ
    print("Code of your pets:", ",".join(map(str, codes)))