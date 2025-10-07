# กำหนด Dictionary สำหรับเก็บรหัสสัตว์เลี้ยง
pet_codes = {
    "Dog": 0,
    "Cat": 1,
    "Fish": 2
}

# รับข้อมูลสัตว์เลี้ยงจากผู้ใช้
# ตัวอย่าง: Dog,Cat,Dog,Fish,Cat
user_input = input("Enter your pets: ")

# แยกข้อความที่ผู้ใช้ป้อนโดยใช้คอมมาเป็นตัวคั่น และเก็บใน List
# .strip() ใช้สำหรับลบช่องว่างหัวท้ายของแต่ละชื่อ
pet_list = [pet.strip() for pet in user_input.split(',')]

# สร้าง List เปล่าสำหรับเก็บรหัสสัตว์เลี้ยงที่แปลงแล้ว
encoded_pets = []


for pet_name in pet_list:

    if pet_name in pet_codes:
      
        encoded_pets.append(str(pet_codes[pet_name]))
    else:
        encoded_pets.append("") 


output_code = ",".join(encoded_pets)

print(f"Code of your pets: {output_code}")