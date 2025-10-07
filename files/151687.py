animals_dict = {'Dog':'0','Cat':'1','Fish':'2'}
x1={'Dog':'[1,0,0]','Cat':'[0,1,0]','Fish':'[0,0,1]'}
pets = input("Enter your pets:")
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
x2=x1[pet1]
x3=x1[pet2]
x4=x1[pet3]
x5=x1[pet4]
x6=x1[pet5]
xxx= f"\n{x2}\n{x3}\n{x4}\n{x5}\n{x6}"
sum_annimals = num1+','+num2+','+num3+','+num4+','+num5
print(f"Code of your pets:{sum_annimals}")
print(f"One-hot vectors:{xxx}")