pet_codes = {"Dog": [1, 0, 0],"Cat": [0, 1, 0],"Fish": [0, 0, 1]}
input_pets = input("Enter your pets: ")
pets = input_pets.split(',')
print("One-hot vectors:"("\n".join(map(str, pets_codes))))