pets = input("Enter your pets: ")
pets2 = pets.split(",")
Dog = [1,0,0]
Cat = [0,1,0]
Fish = [0,0,1]

pets_dict = {'Dog':0,'Cat':1,'Fish':2}
hot_pet = {'Dog':[1,0,0],'Cat':[0,1,0],'Fish':[0,0,1]}

print("Code of your pets: ", end="")
print(pets_dict[pets2[0]],
      pets_dict[pets2[1]],
      pets_dict[pets2[2]],
      pets_dict[pets2[3]],
      pets_dict[pets2[4]], sep=',')

print("One-hot vectors:")
print(hot_pet[pets2[0]],)
print(hot_pet[pets2[1]],)
print(hot_pet[pets2[2]],)
print(hot_pet[pets2[3]],)
print(hot_pet[pets2[4]],)