pet_code = {'Dog': 0, 'Cat': 1, 'Fish': 2}\
one_hot = {0: [1, 0, 0],1: [0, 1, 0],2: [0, 0, 1] }
input_str = input("Enter your pets: ")
pets = input_str.split(',')
v0 = pet_code[pets[0]]
v1 = pet_code[pets[1]]
v2 = pet_code[pets[2]]
v3 = pet_code[pets[3]]
v4 = pet_code[pets[4]]
print("Code of your pets:", str(v0) + "," + str(v1) + "," + str(v2) + "," + str(v3) + "," + str(v4))
print("One-hot vectors:")
print(one_hot[v0])
print(one_hot[v1])
print(one_hot[v2])
print(one_hot[v3])
print(one_hot[v4])