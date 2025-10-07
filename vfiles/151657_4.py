pet_code = {
    "Dog": 0,
    "Cat": 1,
    "Fish": 2
}
pets = input("Enter your pets: ")
pet_list = [pet.strip() for pet in pets.split(",")]
code_list = [str(pet_code[pet]) for pet in pet_list]
print("Code of your pets: " + ",".join(code_list))