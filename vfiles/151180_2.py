pet_codes = {
    "Dog": 0,
    "Cat": 1,
    "Fish":2,
one_hot_vectors = {
    "Dog": [1, 0, 0],
    "Cat": [0, 1, 0],
    "Fish": [0, 0, 1]
}
pets_input = input("Enter your pets: ")
pets_list = pets_input.split(",")

codes = []

for pet in pets_list:
    pet = pet.strip()
    codes.append(str(pet_codes[pet]))

print("Code of your pets:", ",".join(codes))
print("One-hot vectors:")
for pet in pets_list:
    pet = pet.strip()
    print(one_hot_vectors[pet])