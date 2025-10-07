pet = input("Enter your pets: ")
pet_code = {"Dog":0,"Cat":1,"Fish":2}
pet_vector = {"Dog":[1,0,0],"Cat":[0,1,0],"Fish":[0,0,1]}
sp = pet.split(",")
a = pet_code[sp[0]]
a1 = pet_code[sp[1]]
a2 = pet_code[sp[2]]
a3 = pet_code[sp[3]]
a4 = pet_code[sp[4]]
b = pet_vector[sp[0]]
b1 = pet_vector[sp[1]]
b2 = pet_vector[sp[2]]
b3 = pet_vector[sp[3]]

print(f"Code of your pets: {a},{a1},{a2},{a3},{a4}",sep=',')
print(f"One-hot vectors: /n{b}/n{b1}/n{b2}/n{b3}")