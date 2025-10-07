input_pets = input("Enter your pets: ")
pets = input_pets.split(",")
pet_dict = {"Dog": 0,"Cat": 1,"Fish": 2}
code0 = pet_dict[pets[0]]
code1 = pet_dict[pets[1]]
code2 = pet_dict[pets[2]]
code3 = pet_dict[pets[3]]
code4 = pet_dict[pets[4]]
print("Code of your pets:", f"{code0},{code1},{code2},{code3},{code4}")

one_hot = {"Dog":"[1,0,0]","Cat":"[0,1,0]","Fish":"[0,0,1]"}
print("One-hot vectors:",end="\n")
print(one_hot[pets[0]],
      one_hot[pets[1]],
      one_hot[pets[2]],
      one_hot[pets[3]],
      one_hot[pets[4]],sep="\n")