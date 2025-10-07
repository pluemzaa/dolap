num_dict = {"Dog":[1, 0, 0], "Cat":[0, 1, 0], "Fish":[0, 0, 1]}
hex_str = "Dog,Cat,Dog,Fish,Cat"
hex_pet = hex_str.split(",")

pet = input("Enter your pets: ")
pet = pet.split(",")

print("Code of your pets:", end='\n')
print(num_dict[pet[0]],num_dict[pet[1]],num_dict[pet[2]],num_dict[pet[3]],num_dict[pet[4]],sep='\n')