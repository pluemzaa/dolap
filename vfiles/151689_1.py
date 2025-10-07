#input_pet = input("Enter your pets:")
input_pet = input("Enter your pets:")

pet_map = {"Dog"    :   0   , 
           "Cat"    :   1   ,
           "Fish"   :   2   }

pet = input_pet.split(',')

result_code = []

for pet_name in pet : 
    code = pet_map[pet_name]
    result_code.append(code)


output_string = ",".join([str(code) for code in result_code])


print("Code of your pets:" ,output_string)