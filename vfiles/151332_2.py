pets = input("Enter your pets: ")
pets = pets.split(",")
codes = []
for pet in pets:
    if pet.strip() == "Dog":
        codes.append("0")
    elif pet.strip() == "Cat":
        codes.append("1")
    elif pet.strip() == "Fish":
        codes.append("2")
print("Code of your pets:", ",".join(codes))