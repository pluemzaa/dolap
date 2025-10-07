pets = input("Enter your pets: ").split()
pets_list = [pets[0],pets[1],pets[2],pets[3],pets[4]]
pets_dict = {'Dog': 0, 'Cat': 1, 'Fish': 2}
print(pets_dict[pets_list[0]])
print(pets_dict[pets_list[1]])
print(pets_dict[pets_list[2]])
print(pets_dict[pets_list[3]])
print(pets_dict[pets_list[4]])