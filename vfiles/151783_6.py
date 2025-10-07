n1 = input("Enter your pets: ")
n5 = [pet.strip() for pet in n1.split(",")]

pet_code = {"Dog": 0, "Cat": 1, "Fish": 2}

print("Code of your pets: ", end="")
for i in range(len(n5)):
    print(pet_code[n5[i]], end="," if i < len(n5) - 1 else "\n")