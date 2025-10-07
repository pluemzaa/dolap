pet_code={"Dog":[0],"Cat":[1],"Fish":[2]}

pet_text=input("Enter your pets: ")
p=pet_text.split(",")

print("Code of your pets: ",end=" ")
print(pet_code[p[0]][0],",",pet_code[p[1]][0],",",pet_code[p[2]][0],",",pet_code[p[3]][0],",",pet_code[p[4]][0],end=" ")