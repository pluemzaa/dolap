# กำหนดรหัสสัตว์
pet_codes = {
    "Dog": 0,
    "Cat": 1,
    "Fish": 2
}

# กำหนด One-hot vector
one_hot_vectors = {
    "Dog": [1, 0, 0],
    "Cat": [0, 1, 0],
    "Fish": [0, 0, 1]
}

# รับข้อมูลจากผู้ใช้
pets_input = input("Enter your pets: ")

# แปลงข้อมูลเป็น list
pets_list = pets_input.split(",")

# สร้าง list สำหรับเก็บรหัส
codes = []

# แปลงชื่อสัตว์เป็นรหัส
for pet in pets_list:
    pet = pet.strip()
    codes.append(str(pet_codes[pet]))

# แสดงผลรหัสสัตว์
print("Code of your pets:", ",".join(codes))

# แสดงผล One-hot vector
print("One-hot vectors:")
for pet in pets_list:
    pet = pet.strip()
    print(one_hot_vectors[pet])