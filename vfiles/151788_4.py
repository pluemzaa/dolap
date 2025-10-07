pets_code = { 'Dog': 0, 'Cat': 1, 'Fish': 2 }

input_data = input("Enter your pets : ")

pet_list = input_data.split(',')
pet_list = [pet.strip() for pet in pet_list]

print("Code of your pets:", end = " ")
print(Pet_dich[Pet[0]],Pet_dich[Pet[1]],Pet_dich[Pet[2]],Pet_dich[Pet[3]],Pet_dich[Pet[4]], sep =",")