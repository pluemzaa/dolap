pet = input("Enter your pets: ")
sp = pet.split(",")

#dictionary
pet_dic = {"Dog" : 0 , "Cat" : 1 , "Fish" : 2}
a1 = pet_dic[sp[0]]
a2 = pet_dic[sp[1]]
a3 = pet_dic[sp[2]]
a4 = pet_dic[sp[3]]
a5 = pet_dic[sp[4]]


print(a1,a2,a3,a4,a5 , sep=",")