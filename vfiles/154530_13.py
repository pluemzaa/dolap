pet_codes = {
    "Dog": 0,
    "Cat": 1,
    "Fish": 2
}
user_input = input("Enter your pets: ")
pet_list = [pet.strip() for pet in user_input.split(",")]
encoded_list = [str(pet_codes[pet]) for pet in pet_list]
print("Code of your pets:", ",".join(encoded_list))