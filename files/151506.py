def encode_pets():
    pet_codes = {
        "Dog": 0,
        "Cat": 1,
        "Fish": 2
    }

    user_input = input("Enter your pets: ")
    pets_list = user_input.split(',')

    encoded_pets = []
    for pet in pets_list:
        pet = pet.strip()
        if pet in pet_codes:
            encoded_pets.append(str(pet_codes[pet]))

    print("Code of your pets: " + ",".join(encoded_pets))

encode_pets()