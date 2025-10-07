animals_dict = {'Dog':'0','Cat':'1','Fish':'2'}
pets = input("Enter your pets: ")# must input 5 type of pets 
make_pet = pets.split(',')# then split then into list 
pet1 = make_pet[0]# this is the process that tranform list and set index 
pet2 = make_pet[1]
pet3 = make_pet[2]
pet4 = make_pet[3]
pet5 = make_pet[4]

num1 = animals_dict[pet1]# this process find in dict 
num2 = animals_dict[pet2]
num3 = animals_dict[pet3]
num4 = animals_dict[pet4]
num5 = animals_dict[pet5]

sum_annimals = num1+','+num2+','+num3+','+num4+','+num5

print("Code of your pets:" + sum_annimals)
print('One-hot vectors:')
code_of_pet = {'0':'[1, 0, 0]','1':'[0, 1, 0]','2':'[0, 0, 1]'}
sum_again =sum_annimals.split(',')

m1 = sum_again[0]
m2 = sum_again[1]
m3 = sum_again[2]
m4 = sum_again[3]
m5 = sum_again[4]

k1 = code_of_pet[m1]
k2 = code_of_pet[m2]
k3 = code_of_pet[m3]
k4 = code_of_pet[m4]
k5 = code_of_pet[m5]

print(f"{k1}\n{k2}\n{k3}\n{k4}\n{k5}")