pet_code = {'Dog': 0,'Cat': 1,'Fish': 2,}
pet_v = {'Dog': [1, 0, 0],'Cat': [0, 1, 0],'Fish': [0, 0, 1]}

pets = input("Enter your pets:").split(',')

code = pets_code[pets[0]],pets_code[pets[1]],pets_code[pets[2]],pets_code[pets[3]],pets_code[pets[4]]
code_v = pet_v[pets[0]],pet_v[pets[1]],pet_v[pets[2]],pet_v[pets[3]],pet_v[pets[4]]

print("Code of your pets:" + ','.join(map(str,code)))
print(f"One-hot vectors:{code_v}" sep='\n' )