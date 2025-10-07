pet_codes = { "Dog": 0, "Cat": 1, "Fish": 2 }

user_input = input("Enter your pets: ")  
pets_list = user_input.split(',')

encoded_list = [str(pet_codes[pet]) for pet in pets_list]

print("Code of your pets: " + ','.join(encoded_list))