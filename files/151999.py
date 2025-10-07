n1 = input("Enter your pets:")
n5 = n1.split(",")

pet_code = {"Dog": 0, "Cat": 1, "Fish": 2}

print("Code of your pets: ", end="")
print(pet_code[n5[0]],
      pet_code[n5[1]],
      pet_code[n5[2]],
      pet_code[n5[3]],
      pet_code[n5[4]], sep=",")