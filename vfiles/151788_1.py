pets_code = { 'Dog': 0, 'Cat': 1, 'Fish': 2 }

input_data = input("Enter your pets : ")

pet_list = input_data.split(',')
pet_list = [pet.strip() for pet in pet_list]

encoded_list = []

for pet in pet_list:
    if pet in pets_code:
        encoded_list.append(pets_code[pet])
    else:
        print(f"Warning: {pet} is not a valid pet.")
        encoded_list.append(None)

print("Code of your pets: ", ',' .join(str(code) for code in encoded_list))