pet_codes = {'Dog': 0, 'Cat': 1, 'Fish': 2}


pets = input("Enter your pets:").split(',')


encoded_pets = [str(pet_codes[pet.strip()]) for pet in pets]

print("Code of your pets: " + ','.join(encoded_pets))