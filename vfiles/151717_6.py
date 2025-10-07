pet_codes = {
    “Dog”: 0,
    “Cat”: 1,
    “Fish”: 2
}
input_pets = input(“Enter your pets: “)
pet_list = input_pets.split(‘,’)
coded_pets = [pet_codes[pet.strip()] for pet in pet_list]
print(“Code of your pets:”, ‘,’.join(map(str, coded_pets)))