pet_dict = {
    'Dog': (0, [1, 0, 0]),
    'Cat': (1, [0, 1, 0]),
    'Fish': (2, [0, 0, 1])
}

pets_input = input("Enter your pets: ")
pets_split = pets_input.split(',')

pets0 = pets_split[0].strip()
pets1 = pets_split[1].strip()
pets2 = pets_split[2].strip()
pets3 = pets_split[3].strip()
pets4 = pets_split[4].strip()

codes = [
    pet_dict[pets0][0],
    pet_dict[pets1][0],
    pet_dict[pets2][0],
    pet_dict[pets3][0],
    pet_dict[pets4][0]
]

vectors = [
    pet_dict[pets0][1],
    pet_dict[pets1][1],
    pet_dict[pets2][1],
    pet_dict[pets3][1],
    pet_dict[pets4][1]
]

print("Code of your pets:", f"{codes[0]},{codes[1]},{codes[2]},{codes[3]},{codes[4]}")
print("One-hot vectors:")
print(vectors[0])
print(vectors[1])
print(vectors[2])
print(vectors[3])
print(vectors[4])