pets_input = input("Enter your pets: ")
pets = [pet.strip() for pet in pets_input.split(",")]

pet_code = {"Dog": 0, "Cat": 1, "Fish": 2}
pet_onehot = {
    "Dog": [1, 0, 0],
    "Cat": [0, 1, 0],
    "Fish": [0, 0, 1]
}
codes = []
for pet in pets:
    codes.append(str(pet_code[pet]))

print("Code of your pets:", ",".join(codes))
print("One-hot vectors:")
for pet in pets:
    print(pet_onehot[pet])