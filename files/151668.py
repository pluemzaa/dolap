pet_dict = {"Dog":"0" , "Cat":"1" , "Fish":"2"}
pet_hotline = {"Dog":[1,0,0] , "Cat":[0,1,0] , "Fish":[0,0,1]}
pet = input("Enter your pets:")
pet = pet.split(",")
code_pet = pet_dict[pet[0]],pet_dict[pet[1]],pet_dict[pet[2]],pet_dict[pet[3]],pet_dict[pet[4]]
print ("Code of your pets:",",".join(code_pet))
print ('One-hot vectors:\n',pet_hotline[pet[0]],"\n",pet_hotline[pet[1]],"\n",pet_hotline[pet[2]],'\n',pet_hotline[pet[3]],'\n',pet_hotline[pet[4]])