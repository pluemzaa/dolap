pett=input("Enter your pets:")
input_pet= "Dog,Cat,Fish"
pets1=input_pet.split(",")

pet_dict={"Dog":0,"Cat":1,"Fish":2}
print("Code of your pets:",pet_dict[pets1[0]],
      pet_dict[pets1[1]],
      pet_dict[pets1[2]],sep=',')