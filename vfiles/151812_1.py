pet_code = {"Dog":0,"Cat":1,"Fish":2}
pet = input("Enter your pets: ")
pet_vector = {"Dog": [1, 0, 0], "Cat": [0, 1, 0], "Fish": [0, 0, 1]}

sp = pet.split(",")
pv = pet.split(",")
b1 = pet_vector[pv[0]]
b2 = pet_vector[pv[1]]
b3 = pet_vector[pv[2]]
b4 = pet_vector[pv[3]]
b5 = pet_vector[pv[4]]
a1 = pet_code[sp[0]]
a2 = pet_code[sp[1]]
a3 = pet_code[sp[2]]
a4 = pet_code[sp[3]]
a5 = pet_code[sp[4]]

print(f"Code of your pets: {a1},{a2},{a3},{a4},{a5}",sep=',')
print(pv)
print(f"One-hot vectors: \n{b1}\n{b2}\n{b3}\n{b4}\n{b5}",sep = ' ')