pets = input("Enter your pets: ").split(",")
Dict = {"Dog": 0, "Cat": 1, "Fish": 2}

print("Code of your pets: ", end="")
for i in range(len(pets)):
    print(Dict[pets[i]])