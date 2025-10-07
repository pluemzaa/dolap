# กำหนดรหัสสัตว์เลี้ยง
pet_codes = {
    "Dog": 0,
    "Cat": 1,
    "Fish": 2
}

# รับข้อมูลสัตว์เลี้ยงจากผู้ใช้
pets_input = input("Enter your pets: ")

# แยกข้อความด้วยคอมมา
pets_list = pets_input.split(",")

# ตรวจสอบว่าผู้ใช้ป้อนข้อมูลครบ 5 ตัวหรือไม่
if len(pets_list) != 5:
    print("Please enter exactly 5 pet names separated by commas.")
else:
    # แปลงชื่อสัตว์เลี้ยงเป็นรหัส
    encoded = []
    for pet in pets_list:
        pet = pet.strip()  # ลบช่องว่าง
        if pet in pet_codes:
            encoded.append(str(pet_codes[pet]))
        else:
            encoded.append("?")  # หากไม่รู้จักสัตว์นั้น ใส่ ? แทน

    # แสดงผลลัพธ์
    print("Code of your pets:", ",".join(encoded))