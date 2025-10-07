Pet = {"Dog":0,"Cat":1,"Fish":2}
Petnum = {"Dog":[1, 0, 0],"Cat":[0,1,0],"Fish":[0, 0, 1]}
Entr_pet = input("Enter your pets:")
a = Entr_pet.split(",")
print("Code of your pets:",end="")
print(Pet[a[0]], Pet[a[1]], Pet[a[2]], Pet[a[3]], Pet[a[4]], sep=",")
print("One-hot vectors:",end="\n")
print(Petnum[a[0]], Petnum[a[1]], Petnum[a[2]], Petnum[a[3]], Petnum[a[4]], sep="\n")