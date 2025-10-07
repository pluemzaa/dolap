pets = input("Enter your pets: ")

h = {"Dog" : [1, 0, 0], "Cat" : [0, 1, 0], "Fish" : [0, 0, 1]}
h_ = {"Dog" : 0, "Cat" : 1, "Fish" : 2}

pets = pets.split(",")

print(f"Code of your pets: {h_[pets[0]]},{h_[pets[1]]},{h_[pets[2]]},{h_[pets[3]]},{h_[pets[4]]}")
print("One-hot vectors:", h[pets[0]], h[pets[1]], h[pets[2]], h[pets[3]], h[pets[4]], sep="\n")