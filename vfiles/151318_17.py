pets_dict = {'Dog': 0, 'Cat': 1, 'Fish': 2}
pets = input("Enter your pets: ")
pets_list = pets.split(",")
code_1 = str(pets_dict[pets_list[0]])
code_2 = str(pets_dict[pets_list[1]])
code_3 = str(pets_dict[pets_list[2]])
code_4 = str(pets_dict[pets_list[3]])
code_5 = str(pets_dict[pets_list[4]])

print("Code of your pets:", code1 + "," + code2 + "," + code3 + "," + code4 + "," + code5)