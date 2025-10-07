pet=input("Enter your pets:")
pet1=pet.split()
pet_code={"Dog":0,"Cat":1,"Fish":2}
print("Code of your pets:",end="\n")
print(pet_code[pet1[0]],
      pet_code[pet1[1]],
      pet_code[pet1[2]],
      pet_code[pet1[3]],
      pet_code[pet1[4]],sep=',')