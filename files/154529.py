pets = input("Enter your pets: ")
pets2 = pets.split(",")
pets_dict = {'Dog':0,'Cat':1,'Fish':2}


print("Code of your pets: ", end="")
print(pets_dict[pets2[0]],
      pets_dict[pets2[1]],
      pets_dict[pets2[2]],
      pets_dict[pets2[3]],
      pets_dict[pets2[4]], sep=',')