petcode={'Dog':0, 'Cat':1, 'Fish':2}

pet = input('Enter your pets:')
p = pet.split(',')

print("Code of your pets: ",end=" ")
print(petcode[p[0]],",",petcode[p[1]],",",petcode[p[2]],",",petcode[p[3]],",",petcode[p[4]],end=" ")