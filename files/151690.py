pet_codes = {"Dog": 0, "Cat": 1, "Fish": 2}
one_hot_vectors = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

pets = [pet.strip() for pet in input("Enter your pets: ").split(",")]
codes = [pet_codes[pet] for pet in pets]

print("Code of your pets:", ",".join(map(str, codes)))
print("One-hot vectors:")
for code in codes:
    print(one_hot_vectors[code])