pet_code = {'Dog': 0 ,'Cat' : 1 ,'Fish' : 2}
one_hot = {0:[1,0,0],1:[0,1,0],2:[0,0,1]}
pet_input = input("Enter your pets:")
pets = pet_input.split(',')
v1 = pet_code[pets[0]]
v2 = pet_code[pets[1]]
v3 = pet_code[pets[2]]
v4 = pet_code[pets[3]]
v5 = pet_code[pets[4]]
print("Code of your pets:", v1,(","),v2,(","),v3,(","),v4,(","),v5)
print("One-hot vectors:",("\n"), one_hot[v1],("\n"), one_hot[v2],("\n"), one_hot[v3],("\n"), one_hot[v4],("\n"), one_hot[v5])