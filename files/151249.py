pets = input("Enter your pets: ")

h = {"Dog" : 0, "Cat" : 1, "Fish" : 2}

pets = pets.split(",")

print(f"Code of your pets: {h[pets[0]]},{h[pets[1]]},{h[pets[2]]},{h[pets[3]]},{h[pets[4]]}")