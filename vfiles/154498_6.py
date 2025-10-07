pet_codes = {"Dog": 0,"Cat": 1,"Fish": 2}
pet_text = input("Enter your pets: ")
pets = pet_text.split(",")
print("Code of your pets:", pet_codes[pets[0]], pet_codes[pets[1]], pet_codes[pets[2]], pet_codes[pets[3]], pet_codes[pets[4]], sep=",")