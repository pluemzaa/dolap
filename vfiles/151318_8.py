pets = input("Enter your pets: ").split()
pets_list = [pets[0], pets[1],pets[2] ,pets[3] ,pets[4]]
pets_dict = {'Dog': 0, 'Cat': 1, 'Fish': 2}

code_1 = pets_dict[pets_list[0]]
code_2 = pets_dict[pets_list[1]]
code_3 = pets_dict[pets_list[2]]
code_4 = pets_dict[pets_list[3]]
code_5 = pets_dict[pets_list[4]]

print(f"Code for your pets: {code_1}, {code_2}, {code_3}, {code_4}, {code_5}")