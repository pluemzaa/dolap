pet_codes = {
    "Dog": 0,
    "Cat": 1,
    "Fish": 2
}

# รับข้อมูลจากผู้ใช้
user_input = input("Enter your pets: ")

# แยกข้อมูลเป็น list โดยใช้ ',' คั่น และลบช่องว่างออกด้วย strip()
pet_list = [pet.strip() for pet in user_input.split(",")]

# เข้ารหัสสัตว์แต่ละตัวจาก pet_list ด้วย dictionary
encoded_list = [str(pet_codes[pet]) for pet in pet_list]

# แสดงผลลัพธ์
print("Code of your pets:", ",".join(encoded_list))