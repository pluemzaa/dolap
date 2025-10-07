pet_txt=input("Enter your pets: ")
pet= pet_txt.split(",")

pet_num= {"Dog":[0],"Cat":[1],"Fish":[2]}
g= pet_txt.split(",")
#print("Result",end=" ")
print(pet_num[g[0]],",",pet_num[g[1]],",",pet_num[g[2]],pet_num[g[3]],pet_num[g[4]],sep="")