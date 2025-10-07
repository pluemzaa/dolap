pete= {"Dog": 0,"Cat": 1,"Fish": 2}
pet_one_hot = {"Dog": [1, 0, 0],"Cat": [0, 1, 0],"Fish": [0, 0, 1]}
pets = input("Enter your pets: ")
pet_list = [pet.strip() for pet in pets.split(",")]
code_list = [str(pete[pet]) for pet in pet_list]
print("Code of your pets: " + ",".join(code_list))
print("One-hot vectors:")
for pet in pet_list:
    print(pet_one_hot[pet])