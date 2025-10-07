# Create dictionary to map pet names to codes
pet_to_code = {
    "Dog": 0,
    "Cat": 1,
    "Fish": 2
}

# Create dictionary to map pet names to one-hot vectors
pet_to_onehot = {
    "Dog": [1, 0, 0],
    "Cat": [0, 1, 0],
    "Fish": [0, 0, 1]
}

# Ask user to input 5 pet names separated by comma
user_input = input("Enter 5 pet names (choose from Dog, Cat, Fish): ")
pets = user_input.split(',')

# Remove extra spaces
pets = [pet.strip() for pet in pets]

# Convert pets to codes
codes = [pet_to_code[pet] for pet in pets]

# Convert pets to one-hot vectors
onehots = [pet_to_onehot[pet] for pet in pets]

# Print results
print("Code of your pets:", ','.join(map(str, codes)))
print("One-hot vectors:")
for vec in onehots:
    print(vec)