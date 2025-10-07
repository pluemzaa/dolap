# Dictionary for pet name to code
pet_to_code = {
    "Dog": 0,
    "Cat": 1,
    "Fish": 2
}

# Dictionary for one-hot vector
pet_to_onehot = {
    "Dog": [1, 0, 0],
    "Cat": [0, 1, 0],
    "Fish": [0, 0, 1]
}

# Input
user_input = input("Enter your pets (e.g. Dog,Cat,Dog,Fish,Cat): ")
pets = user_input.split(',')

# Show code
codes = [str(pet_to_code[pet]) for pet in pets]
print("Code of your pets: " + ",".join(codes))

# Show one-hot vectors in Dolab format (no space)
print("One-hot vectors:")
for pet in pets:
    onehot = pet_to_onehot[pet]
    print(f"[{onehot[0]},{onehot[1]},{onehot[2]}]")