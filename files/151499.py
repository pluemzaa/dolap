pet_to_code = {
    "Dog": 0,
    "Cat": 1,
    "Fish": 2
}

code_to_onehot = {
    0: [1, 0, 0],
    1: [0, 1, 0],
    2: [0, 0, 1]
}
pets = input("Enter your pets: ")
pet_list = list(map(str.strip, pets.split(",")))
assert len(pet_list) == 5, "Please enter exactly 5 pets."
codes = list(map(pet_to_code.get, pet_list))
print("Code of your pets:", ",".join(map(str, codes)))
onehot_vectors = list(map(code_to_onehot.get, codes))
print("One-hot vectors:")
print(*onehot_vectors, sep="\n")