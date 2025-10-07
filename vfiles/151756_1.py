# Dictionary to store codes for each pet
pet_codes = {
    "Dog": 0,
    "Cat": 1,
    "Fish": 2
}

# Dictionary to store one-hot vectors
one_hot_vectors = {
    "Dog": [1, 0, 0],
    "Cat": [0, 1, 0],
    "Fish": [0, 0, 1]
}

# Get input from the user
pets_input = input("Enter your pets (separated by commas): ")

# Split the input into a list
pets_list = pets_input.split(',')

# Show the pet codes
codes = [str(pet_codes[pet]) for pet in pets_list]
print("Code of your pets:", ",".join(codes))

# Show the one-hot vectors
print("One-hot vectors:")
for pet in pets_list:
    print(one_hot_vectors[pet])