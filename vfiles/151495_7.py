pets = input("Enter your pets:").split(",")

pets_code = {"Dog": 0,"Cat": 1,"Fish": 2}

code = pets_code[pets[0]],pets_code[pets[1]],pets_code[pets[2]],pets_code[pets[3]],pets_code[pets[4]]

print("Code of your pets:" + ','.join(encoded_pets))