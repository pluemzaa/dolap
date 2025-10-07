codes = {'Dog': '0', 'Cat': '1', 'Fish': '2'}
pets = input("Enter your pets: ")
pet_list = pets.split(',')

code1 = codes[pet_list[0]]
code2 = codes[pet_list[1]]
code3 = codes[pet_list[2]]
code4 = codes[pet_list[3]]
code5 = codes[pet_list[4]]

print("Code of your pets:", code1 + "," + code2 + "," + code3 + "," + code4 + "," + code5)