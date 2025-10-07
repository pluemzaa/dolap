# Dictionary for pet name to code
pet_to_code = {
    "Dog": 0,
    "Cat": 1,
    "Fish": 2
}

# Dictionary for pet name to one-hot vector
pet_to_onehot = {
    "Dog": [1,0,0],
    "Cat": [0,1,0],
    "Fish": [0,0,1]
}

# Input from user
user_input = input("Enter your pets (e.g. Dog,Cat,Dog,Fish,Cat): ")

# Split input string into list
pets = user_input.split(',')

# Convert pet names to code
codes = [str(pet_to_code[pet]) for pet in pets]
print("Code of your pets: " + ",".join(codes))

# Print One-hot vectors
print("One-hot vectors:")
for pet in pets:
    print(pet_to_onehot[pet])