pets_input = input("Enter your pets: ")
pets = pets_input.split(',')
pet_code = {"Dog": 0, "Cat": 1, "Fish": 2}
pet_vector = {
    "Dog": [1, 0, 0],
    "Cat": [0, 1, 0],
    "Fish": [0, 0, 1]
}

print("Code of your pets:", end=' ')
codes = [str(pet_code[pet]) for pet in pets]
print(",".join(codes))

print("One-hot vectors:")
for pet in pets:
    print(pet_vector[pet])