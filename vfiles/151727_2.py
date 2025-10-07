pet_to_code = {
    'Dog': 0,
    'Cat': 1,
    'Fish': 2
}

pet_to_onehot = {
    'Dog': [1, 0, 0],
    'Cat': [0, 1, 0],
    'Fish': [0, 0, 1]
}
pets = input('Enter your pets: ').split(',')
pets = [pet.strip() for pet in pets]
codes = [str(pet_to_code[pet]) for pet in pets]
print('Code of your pets:', ','.join(codes))
print('One-hot vectors:')
for pet in pets:
    print(pet_to_onehot[pet])