pet=input("Enter your pets:")
pet1=pet.split(",")
pet_code={"Dog":0,"Cat":1,"Fish":2}
print("Code of your pets:",end="")
print(pet_code[pet1[0]],
      pet_code[pet1[1]],
      pet_code[pet1[2]],
      pet_code[pet1[3]],
      pet_code[pet1[4]],sep=',')
pet_vector={"Dog":[1, 0, 0],"Cat":[0, 1, 0],"Fish":[0, 0, 1]}
print("One-hot vectors:",end="\n")
print(pet_vector[pet1[0]],
      pet_vector[pet1[1]],
      pet_vector[pet1[2]],
      pet_vector[pet1[3]],
      pet_vector[pet1[4]],sep='\n')