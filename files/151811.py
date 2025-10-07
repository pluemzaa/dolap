# Dog = 0
# Cat = 1
# Fish = 2

pet = input("Enter your pets: ")
pet_code = {"Dog":0,"Cat":1,"Fish":2}
sp = pet.split(",")
Dog = pet_code[sp[0]]
a1 = pet_code[sp[1]]
a2 = pet_code[sp[2]]
as2 = pet_code[sp[3]]
aa = pet_code[sp[4]]

print(f"Code of your pets: {Dog},{a1},{a2},{as2},{aa}",sep=',')