pets = input("Enter your pets: ").split(",")

pets_code = {"Dog": 0, "Cat": 1, "Fish": 2}

code = [pets_code[pet.strip()] for pet in pets]

print("Code of your pets: " + ','.join(encoded_pets))