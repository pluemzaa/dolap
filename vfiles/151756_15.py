CJ = {'Dog': 0, 'Cat': 1, 'Fish': 2}
pets = input("Enter your pets: ")
pets_numm = pets.split(',')

pet1 = pets_numm[0]
pet2 = pets_numm[1]
pet3 = pets_numm[2]
pet4 = pets_numm[3]
pet5 = pets_numm[4]

num1 = CJ[pet1]
num2 = CJ[pet2]
num3 = CJ[pet3]
num4 = CJ[pet4]
num5 = CJ[pet5]

hog = str(num1) + ',' + str(num2) + ',' + str(num3) + ',' + str(num4) + ',' + str(num5) + ','
print("Code of your pets: " + hog)

print("One-hot vectors:")
numhow = ["[1, 0, 0]", "[0, 1, 0]", "[0, 0, 1]"]
print(numhow[num1])
print(numhow[num2])
print(numhow[num3])
print(numhow[num4])
print(numhow[num5])