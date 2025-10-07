pet_code = {'Dog': 0,'Cat': 1,'Fish': 2}
onehot_vector = {'Dog': [1, 0, 0],'Cat': [0, 1, 0],'Fish': [0, 0, 1]}

pets = input("Enter your pets: ")  
pets_list = pets.split(',')
if len(pets_list) != 5:
    print("กรุณากรอกชื่อสัตว์เลี้ยงจำนวน 5 ชื่อ คั่นด้วย , ตัวอย่างเช่น Dog,Cat,Dog,Fish,Cat")
else:
    code_list = []
    onehot_list = []
    for pet in pets_list:
        pet = pet.strip()  
        code_list.append(str(pet_code[pet]))
        onehot_list.append(onehot_vector[pet])
    
    print("Code of your pets: " + ','.join(code_list))
    print("One-hot vectors:")
    for vector in onehot_list:
        print(vector)