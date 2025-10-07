animals_dict = {'Dog':'0','Cat':'1','Fish':'2'}
pets = input("Enter your pet: ")
make_pet = pets.split(',')
pet1 = make_pet[0]
pet2 = make_pet[1]
pet3 = make_pet[2]
pet4 = make_pet[3]
pet5 = make_pet[4]

num1 = animals_dict[pet1]
num2 = animals_dict[pet2]
num3 = animals_dict[pet3]
num4 = animals_dict[pet4]
num5 = animals_dict[pet5]

sum_annimals = num1+','+num2+','+num3+','+num4+','+num5

print(f"Code of your pets:{sum_annimals}")