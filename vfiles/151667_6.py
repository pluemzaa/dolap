Pet_dict = {"Dog": 0, "Cat": 1, "Fish": 2}
Pet = input("Enter your pet:")
Pet = Pet.split(",")
print("Code of your pet:", end = " ")
print(Pet_dict[Pet[0]],Pet_dict[Pet[1]],Pet_dict[Pet[2]],Pet_dict[Pet[3]],Pet_dict[Pet[4]], sep = ",")