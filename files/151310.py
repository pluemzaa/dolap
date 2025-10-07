pet_dict = {"Dog":0, "Cat":1, "Fish":2}

pet = input("Enter your pets:")
pet = pet.split(",")
print ("Code of your pets:",end=" ")
print (pet_dict[pet[0]],pet_dict[pet[1]],pet_dict[pet[2]],pet_dict[pet[3]],pet_dict[pet[4]],sep=",")