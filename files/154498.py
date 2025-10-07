pet_codes = {"Dog": 0,"Cat": 1,"Fish": 2}
pet_codes1 = {"Dog":[1, 0, 0],"Cat":	[0, 1, 0],"Fish":[0, 0, 1]}
pet_text = input("Enter your pets: ")
pets = pet_text.split(",")
print("Code of your pets :", pet_codes[pets[0]],",", pet_codes[pets[1]],",", pet_codes[pets[2]],",", pet_codes[pets[3]],",", pet_codes[pets[4]])
print("One-hot vectors:", pet_codes1[pets[0]], pet_codes1[pets[1]], pet_codes1[pets[2]], pet_codes1[pets[3]], pet_codes1[pets[4]],sep="\n")