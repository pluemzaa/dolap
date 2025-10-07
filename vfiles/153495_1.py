ai = {'Dog':'0','Cat':'1','Fish':'2'}
pets = input("Enter your pets")
pets_numm = pets.split(',')
pet1=pets_numm[0]
pet2=pets_numm[1]
pet3=pets_numm[2]
pet4=pets_numm[3]
pet5=pets_numm[4]
num1=ai[pet1]
num2=ai[pet2]
num3=ai[pet3]
num4=ai[pet4]
num5=ai[pet5]
hog = num1+','+num2+','+num3+','+num4+','+num5
print("Code of your pets:"+hog)