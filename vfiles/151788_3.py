pets_code = { 'Dog': 0, 'Cat': 1, 'Fish': 2 }

input_data = input("Enter your pets : ")

pet_list = input_data.split(',')
pet_list = [pet.strip() for pet in pet_list]

animal_list = [pets_code[pet] for pet in pet_list]


print("Code of your pets: ", ',' .join(str(code) for code in animal_list))