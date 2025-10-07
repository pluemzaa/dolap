steps=input('Enter your pets:')
input_pet = 'Dog,Cat,Fish'
pet = input_pet.split(',')
print(pet[0])
pet_dict = {'Dog':0,'Cat':1,'Fish':2}
print('Code of your pets:', end=' ')
print(pet_dict[pet[0]],
      pet_dict[pet[1]],
      pet_dict[pet[2]],sep=',')