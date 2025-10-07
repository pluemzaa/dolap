pet_code = {'Dog': 0, 'Cat': 1, 'Fish': 2}
pet_onehot = {'Dog': [1, 0, 0],'Cat': [0, 1, 0],'Fish': [0, 0, 1]}

pets_input = input("Enter your pets: ")
pets_list = [pet.strip() for pet in pets_input.split(',')]

pet1 = str(pet_code[pets_list[0]])
pet2 = str(pet_code[pets_list[1]])
pet3 = str(pet_code[pets_list[2]])
pet4 = str(pet_code[pets_list[3]])
pet5 = str(pet_code[pets_list[4]])

print("Code of your pets: " + ",".join([pet1, pet2, pet3, pet4, pet5]))
print("One-hot vectors:")
print(pet_onehot[pets_list[0]])
print(pet_onehot[pets_list[1]])
print(pet_onehot[pets_list[2]])
print(pet_onehot[pets_list[3]])
print(pet_onehot[pets_list[4]])