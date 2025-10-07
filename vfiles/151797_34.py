pet = input("Enter your pets: ")
pets = pet.split(",")
pet_dict = {"Dog":0,"Cat":1,"Fish":2}
print("Code of your pets:", end=" ")
print(pet_dict[pets[0]],pet_dict[pets[1]],pet_dict[pets[2]],pet_dict[pets[3]],pet_dict[pets[4]],sep=",")

pet2_dict = {"Dog":[1,0,0],"Cat":[0,1,0],"Fish":[0,0,1]}
print("One-hot vectors:", end="\n")
print(pet2_dict[pets[0]],pet2_dict[pets[1]],pet2_dict[pets[2]],pet2_dict[pets[3]],pet2_dict[pets[4]],sep="")