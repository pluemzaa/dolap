Pet_dict = {"Dog": 0, "Cat": 1, "Fish": 2}

Pet = input("Enter your pets:")
Pet = Pet.split(",")

print("Code of your pets:", end = " ")
print(Pet_dict[Pet[0]], Pet_dict[Pet[1]], Pet_dict[Pet[2]], Pet_dict[Pet[3]], Pet_dict[Pet[4]], sep = ",")

O = {"Dog": [1, 0, 0], "Cat": [0, 1, 0], "Fish": [0, 0, 1]}

print("one-hot vectors:", end = "\n")
print(O[Pet[0]],O[Pet[1]],O[Pet[2]],O[Pet[3]],O[Pet[4]], sep = "\n")