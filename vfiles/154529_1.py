pets = input("Enter your pets: ")
pets2 = pets.split()
pets_dict = {"Dog":0,"Cat":1,"Fish":2}
print("Code of your pets: ", end="")
print(pets_dict["Dog"],
      pets_dict["Cat"],
      pets_dict["Dog"],
      pets_dict["Fish"],
      pets_dict["Cat"],sep=","
      )