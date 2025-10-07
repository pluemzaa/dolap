ANi = {'Dog': '0', 'Cat': '1', 'Fish': '2'}
pets = input("Enter your pets: ")
pets_numm = pets.split(',')
pet1 = pets_numm[0]
pet2 = pets_numm[1]
pet3 = pets_numm[2]
pet4 = pets_numm[3]
pet5 = pets_numm[4]
num1 = Ani[pet1]
num2 = ANi[pet2]
num3 = ANi[pet3]
num4 = ANi[pet4]
num5 = ANi[pet5]
hog = num1 + ',' + num2 + ',' + num3 + ',' + num4 + ',' + num5
print("Code of your pets:" + hog)
print("One-hot vectors:")
numa = [ "[1, 0, 0]", "[0, 1, 0]", "[0, 0, 1]" ]
print(numa[int(num1)])
print(numa[int(num2)])
print(numa[int(num3)])
print(numa[int(num4)])
print(numa[int(num5)])