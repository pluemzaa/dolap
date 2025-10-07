C = {'Dog': '0', 'Cat': '1', 'Fish': '2'}
pets = input("Enter your pets: ")
pets_numm = pets.split(',')
pet1 = pets_numm[0]
pet2 = pets_numm[1]
pet3 = pets_numm[2]
pet4 = pets_numm[3]
pet5 = pets_numm[4]
num1 = C[pet1]
num2 = C[pet2]
num3 = C[pet3]
num4 = C[pet4]
num5 = C[pet5]
hog = num1 + ':' + num2 + ':' + num3 + ':' + num4 + ':' + num5
print("Code of your pets:" + hog)