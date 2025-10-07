pet_code = {
    "Dog": 0,
    "Cat": 1,
    "Fish": 2
}


pets_input = input("Enter your pets: ")
pets = [pet.strip() for pet in pets_input.split(",")]


codes = [str(pet_code[pet]) for pet in pets]


print("Code of your pets: " + ",".join(codes))