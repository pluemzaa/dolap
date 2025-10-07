pet_codes = {"Dog": 0,"Cat": 1,"Fish": 2}
user_input = input("Enter your pets: ")
pet_list = user_input.split(",")
encoded_list = []
for pet in pet_list:
    pet = pet.strip()  
    if pet in pet_codes:
        encoded_list.append(str(pet_codes[pet]))
    else:
        encoded_list.append("Error")
print("Code of your pets:", ",".join(encoded_list))