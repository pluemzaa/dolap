pet_codes = {"Dog": [1, 0, 0],"Cat": [0, 1, 0],"Fish": [0, 0, 1]}
input_pets = input("Enter your pets: ")
pets = input_pets.split(',')
print("Code of your pets:", ",".join(map(str, pet_codes)))