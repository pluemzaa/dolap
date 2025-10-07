pet_code = {'Dog': 0,'Cat': 1,'Fish': 2}
input_str = input("Enter your pets: ")
pets = input_str.split(',')
v1 = pet_code[pets[0]]
v2 = pet_code[pets[1]]
v3 = pet_code[pets[2]]
v4 = pet_code[pets[3]]
v5 = pet_code[pets[4]]
print("Code of your pets:",v1[0]*v2[0]+v1[1]*v2[1]+v1[2]*v2[2]+v1[3]*v2[3]+v1[4]*v2[4])