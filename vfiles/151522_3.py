# กำหนดรหัสและ One-hot vector สำหรับสัตว์แต่ละชนิด
# รวมข้อมูลไว้ใน Dictionary เดียวกันเพื่อให้จัดการง่ายขึ้น
animal_data = {
    "Dog": {"code": 0, "vector": [1, 0, 0]},
    "Cat": {"code": 1, "vector": [0, 1, 0]},
    "Fish": {"code": 2, "vector": [0, 0, 1]}
}

# รับข้อมูลสัตว์เลี้ยงจากผู้ใช้
pets_input = input("Enter your pets (comma-separated, 5 names): ")

# แยกชื่อสัตว์เลี้ยงออกจากกันและลบช่องว่างหัวท้าย
pets_list = [pet.strip() for pet in pets_input.split(',')]

# ตรวจสอบจำนวนชื่อสัตว์
if len(pets_list) != 5:
    print("Error: Please enter exactly 5 pet names.")
else:
    # ใช้ List Comprehension เพื่อสร้างลิสต์ของรหัสและ One-hot vector
    # พร้อมจัดการกับชื่อที่ไม่รู้จักในลูปเดียวกัน
    coded_pets = []
    vectors_output = []

    for pet_name in pets_list:
        if pet_name in animal_data:
            coded_pets.append(str(animal_data[pet_name]["code"]))
            vectors_output.append(animal_data[pet_name]["vector"])
        else:
            print(f"Warning: '{pet_name}' is not a recognized pet type. Skipping.")
            coded_pets.append("N/A")
            vectors_output.append("N/A")


    print("Code of your pets: " + ",".join(coded_pets))
    print("One-hot vectors:")
    for vector in vectors_output:
        print(vector)