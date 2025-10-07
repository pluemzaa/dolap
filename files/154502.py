num_dict = {
    "Dog": [1, 0, 0],
    "Cat": [0, 1, 0],
    "Fish": [0, 0, 1]
}

label_dict = {
    "Dog": 0,
    "Cat": 1,
    "Fish": 2
}

pet_input = input("Enter your pets: ")
pet_list = pet_input.split(",")


codes = [str(label_dict[pet]) for pet in pet_list]
print("Code of your pets:", ",".join(codes))


print("One-hot vectors:")
for pet in pet_list:
    print(num_dict[pet])