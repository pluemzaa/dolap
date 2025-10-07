Pet_dich = {"Dog": 0, "Cat": 1, "Fish": 2}

Pet = input("Enter your pet:")
Pet = Pet.split(",")

print("Code of you pet:", end = " ")
print(Pet_dich[Pet[0]],Pet_dich[Pet[1]],Pet_dich[Pet[2]],Pet_dich[Pet[3]],Pet_dich[Pet[4]], sep =",")