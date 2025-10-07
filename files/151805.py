pet_code = {'Dog': 0,'Cat': 1,'Fish': 2}
pets = input("Enter your pets: ")  
pets_list = pets.split(',')
code_list = []
for pet in pets_list:
    pet = pet.strip()
    code_list.append(str(pet_code[pet]))
print("Code of your pets: " + ','.join(code_list))