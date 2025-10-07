pets = input("Enter your pets: ")
pets = pets.split(",")
codes = []
onehot = []
for pet in pets:
    pet = pet.strip()
    if pet == "Dog":
        codes.append("0")
        onehot.append([1, 0, 0])
    elif pet == "Cat":
        codes.append("1")
        onehot.append([0, 1, 0])
    elif pet == "Fish":
        codes.append("2")
        onehot.append([0, 0, 1])
print("Code of your pets:", ",".join(codes))
print("One-hot vectors:")
for v in onehot:
    print()