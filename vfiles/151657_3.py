# สร้าง dictionary เพื่อเก็บ mapping ชื่อสัตว์กับรหัส
pet_code = {
    "Dog": 0,
    "Cat": 1,
    "Fish": 2
}

# รับค่าชื่อสัตว์จากผู้ใช้ (คั่นด้วย ,)
pets = input("Enter your pets: ")

# แยกชื่อสัตว์แต่ละตัวใน list แล้วตัดช่องว่างหน้าหลังออก
pet_list = [pet.strip() for pet in pets.split(",")]

# แปลงชื่อสัตว์เป็นรหัสตามที่กำหนด
code_list = [str(pet_code[pet]) for pet in pet_list]

# รวมรหัสแต่ละตัวด้วยเครื่องหมาย , เพื่อแสดงผล
print("Code of your pets: " + ",".join(code_list))