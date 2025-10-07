#print('Hello Python!')
Pets_num = ("Dog" : 0,"Cat" : 1,"Fish" : 2 )
Pet_one_hot = ("Dog" : [1, 0, 0], "Cat" : [0, 1, 0], "Fish" : [0, 0, 1])
Pets = str(input("Enter your pets "))
Pets_1 = Pets.split(",")
print("Code of your pets:", end='')
print(Pets_num[Pets_1[0]],
Pets_num[Pets_1[1]],
Pets_num[Pets_1[2]],
Pets_num[Pets_1[3]],
Pets_num[Pats_1[4]], sep=',')
print("One hot vectors:", end='\n')
print(Pet_one_hot[Pets_1[0]],
Pets_one_hot[Pets_1[1]],
Pets_one_hot[Pets_1[2]],
Pets_one_hot[Pets_1[3]],
Pets_one_hot[Pats_1[4]], sep='\n')