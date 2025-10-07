pet = input("Enter your pets: ")
pet_c = {"Dog":0,"Cat":1,"Fish":2}
pet_v = {"Dog":[1,0,0],"Cat":[0,1,0],"Fish":[0,0,1]}
sp = pet.split(",")
a = pet_c[sp[0]]
a1 = pet_c[sp[1]]
a2 = pet_c[sp[2]]
a3 = pet_c[sp[3]]
a4 = pet_c[sp[4]]
b = pet_v[sp[0]]
b1 = pet_v[sp[1]]
b2 = pet_v[sp[2]]
b3 = pet_v[sp[3]]
b4 = pet_v[sp[4]]

print(f"Code of your pets: {a},{a1},{a2},{a3},{a4}",sep=',')
print(f"One-hot vectors: \n{b}\n{b1}\n{b2}\n{b3}\n{b4}")