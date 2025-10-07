animals={"Dog":[0],"Cat":[1],"Fish":[2]}

pet=input("Enter your pets: ")
p=pet.split(",")

print("Code of your pets: ",end=" ")
print(animals[p[0]][0],",",animals[p[1]][0],",",animals[p[2]][0],",",animals[p[3]][0],",",animals[p[4]][0],end=" ")