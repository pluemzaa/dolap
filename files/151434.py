Pets_num = {"Dog" : 0, "Cat" : 1, "Fish" : 2 }
Pets = str(input("Enter your pets: "))
Pets_1 = Pets.split(",")

print("Code of your pets:", end='')
print(Pets_num[Pets_1[0]],
Pets_num[Pets_1[1]],
Pets_num[Pets_1[2]],
Pets_num[Pets_1[3]],
Pets_num[Pets_1[4]], sep=',')