pet_code = { 'Dog': 0, 'Cat': 1, 'Fish': 2 }
pets = input("Enter your pets: ")  
pets_list = pets.split(',')
if len(pets_list) != 5:
    print("กรุณากรอกชื่อสัตว์เลี้ยงจำนวน 5 ชื่อ คั่นด้วย , ตัวอย่างเช่น Dog,Cat,Dog,Fish,Cat")
else:
    code_list = []
    for pet in pets_list:
        pet = pet.strip()
        if pet in pet_code:
            code_list.append(str(pet_code[pet]))
        else:
            print(f"ไม่พบสัตว์เลี้ยงชื่อ '{pet}' ในระบบ")
            break
    else:
        print("Code of your pets: " + ','.join(code_list))