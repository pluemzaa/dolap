anm = input("Enter your pets: ")
anms = anm.split(",")
pet = {"Dog":0,"Cat":1,"Fish":2}
print("Code of your pets: ", end=" " )
print(pet[anms[0]],
      pet[anms[1]],
      pet[anms[2]],
      pet[anms[3]],
      pet[anms[4]],sep=",")
pet1={"Dog":[1,0,0],
"Cat":[0,1,0],
"Fish":[0,0,1]}
print("One-hot vectors: ")
print(pet1[anms[0]])
print(pet1[anms[1]])
print(pet1[anms[2]])
print(pet1[anms[3]])
print(pet1[anms[4]])