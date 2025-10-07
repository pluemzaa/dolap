# Create a dictionary that maps pet names to numbers
pet_to_code = {
    "Dog": 0,
    "Cat": 1,
    "Fish": 2
}

# Create a dictionary that maps pet names to one-hot vectors
pet_to_onehot = {
    "Dog": [1, 0, 0],
    "Cat": [0, 1, 0],
    "Fish": [0, 0, 1]
}

# Get input from user
user_input = input("Enter your pets (e.g. Dog,Cat,Dog,Fish,Cat): ")

# Split the input into a list
pets = user_input.split(',')

# Convert pet names to codes
codes = [str(pet_to_code[pet]) for pet in pets]
print("Code of your pets:", ','.join(codes))

# Convert pet names to one-hot vectors
print("One-hot vectors:")
for pet in pets:
    print(pet_to_onehot[pet])