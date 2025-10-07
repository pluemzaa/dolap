n1 = input("Enter your pets: ")
n5 = n1.split(",")

pet1 = n5[0].strip()
pet2 = n5[1].strip()
pet3 = n5[2].strip()
pet4 = n5[3].strip()
pet5 = n5[4].strip()

pet_code = {"Dog": 0, "Cat": 1, "Fish": 2}

print("Code of your pets: ", end="")
print(
    pet_code[pet1], ",",
    pet_code[pet2], ",",
    pet_code[pet3], ",",
    pet_code[pet4], ",",
    pet_code[pet5],
    sep=""
)