anm = input("Enter your pets: ")
#anm = "Dog,Cat,Fish"
#print(anms[0])
anms = anm.split(",")
pet = {"Dog":0,"Cat":1,"Fish":2}
print("Code of your pets: ", end=" " )
print(pet[anms[0]],
      pet[anms[1]],
      pet[anms[2]],
      pet[anms[3]],
      pet[anms[4]],sep=",")