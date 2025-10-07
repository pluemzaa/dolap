input_pets = input("Enter your pets: ")
pets = input_pets.split(",")
pet_dict = {"Dog": 0,"Cat": 1,"Fish": 2}
code0 = pet_dict[pets[0]]
code1 = pet_dict[pets[1]]
code2 = pet_dict[pets[2]]
code3 = pet_dict[pets[3]]
code4 = pet_dict[pets[4]]
print("Code of your pets:", f"{code0},{code1},{code2},{code3},{code4}")