pet_str = input("Enter your pets: ")
pet_code = { "Dog" : 0, "Cat" : 1, "Fish" : 2}

s = pet_str.split(",") 

print(f"code of your pets: {pet_code[s[0]]},{pet_code[s[1]]},{pet_code[s[2]]},{pet_code[s[3]]},{pet_code[s[4]]}")