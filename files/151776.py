num_dict = {"Dog":(0,[1,0,0]), "Cat":(1,[0,1,0]), "Fish":(2,[0,0,1])}
hnum = input("Enter your pets: ")
hnum = hnum.split(",")
p0 = num_dict[hnum[0]]
p1 = num_dict[hnum[1]]
p2 = num_dict[hnum[2]]
p3 = num_dict[hnum[3]]
p4 = num_dict[hnum[4]]
print("Code of your pets:", f"{p0[0]},{p1[0]},{p2[0]},{p3[0]},{p4[0]}")
print('One-hotvectors:',end='\n')
print(p0[1])
print(p1[1])
print(p2[1])
print(p3[1])
print(p4[1])