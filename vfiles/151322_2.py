pet_codes = {
    "Dog": 0,
    "Cat": 1,
    "Fish": 2
}


user_input = input("Enter your pets: ")


pet_list = [pet.strip() for pet in user_input.split(',')]


encoded_pets = []


for pet_name in pet_list:

    if pet_name in pet_codes:
      
        encoded_pets.append(str(pet_codes[pet_name]))
    else:
        encoded_pets.append("") 


output_code = ",".join(encoded_pets)

print(f"Code of your pets: {output_code}")