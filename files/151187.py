pet_txt=input("Enter your pets: ")

pet_num= {"Dog":0,"Cat":1,"Fish":2}
g= pet_txt.split(",")
one={"Dog":[1,0,0],"Cat":[0,1,0],"Fish":[0,0,1]}

print("Code of your pets: ",end=" ")
print(pet_num[g[0]],",",pet_num[g[1]],",",pet_num[g[2]],",",pet_num[g[3]],",",pet_num[g[4]],sep="")
print("One-hot vectors:")
print(one[g[0]])
print(one[g[1]])
print(one[g[2]])
print(one[g[3]])
print(one[g[4]])