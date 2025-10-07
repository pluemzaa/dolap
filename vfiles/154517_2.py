# One-hot encoding dictionary
num_dict = {"Dog": [1, 0, 0], "Cat": [0, 1, 0], "Fish": [0, 0, 1]}

# Input
hex_str = input("Enter your pets (separated by space, e.g., 'Dog Cat Fish Dog Fish'): ")

# Split the input into a list of pet names
pet_list = hex_str.split()

# Validate input
for pet in pet_list:
    if pet not in num_dict:
        print(f"Unknown pet: {pet}")
        exit(1)

# Print one-hot encoded vectors
print("One-hot vectors:")
for pet in pet_list:
    print(num_dict[pet])