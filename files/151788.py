pets_code =  {"Dog": 0, "Cat": 1, "Fish": 2}

pet_list = input("Enter your pets : ")

pet_list = pet_list.split(",")

print("Code of your pets:", end = " ")
print(pets_code[pet_list[0]],pets_code[pet_list[1]],pets_code[pet_list[2]],pets_code[pet_list[3]],pets_code[pet_list[4]], sep =",")