pets_input = input("Enter your pets (separated by commas): ")
pets = pets_input.split(",")

pet_code = {"Dog": 0, "Cat": 1, "Fish": 2}
pet_onehot = {
    "Dog": [1, 0, 0],
    "Cat": [0, 1, 0],
    "Fish": [0, 0, 1]
}

codes = []
print("Code of your pets:", end=" ")

for pet in pets:
    pet = pet.strip()
    if pet in pet_code:
        codes.append(str(pet_code[pet]))  

print(",".join(codes))

print("One-hot vectors:")
for pet in pets:
    pet = pet.strip()
    if pet in pet_onehot:
        print(pet_onehot[pet])