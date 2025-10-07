pets_dict = input("Enter your pets: ")
pets = pets_dict.split(",")
pets_dict = {"Dog":0, "Cat":1, "Fish":2}
#pets = pets_dict.split(",")
print("Code of your pets:",end=" ")
print(pets_dict[pets[0]],
      pets_dict[pets[1]],
      pets_dict[pets[2]],
      pets_dict[pets[3]],
      pets_dict[pets[4]],sep=',')

vector_dict = {"Dog":[1, 0, 0],"Cat":[0, 1, 0],"Fish":[0, 0, 1]}
print("One-hot vectors: ",)
print(vector_dict[pets[0]])
print(vector_dict[pets[1]])
print(vector_dict[pets[2]])
print(vector_dict[pets[3]])
print(vector_dict[pets[4]])