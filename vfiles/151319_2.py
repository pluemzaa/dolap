pet_code = {"Dog": 0, "Cat": 1, "Fish": 2}

pet_text = input("Enter your pets: ")

pets = pet_text.split(",")

print(pets)

print(pet_code[pets[0].strip()], ",", 
      pet_code[pets[1].strip()], ",", 
      pet_code[pets[2].strip()], ",", 
      pet_code[pets[3].strip()], ",", 
      pet_code[pets[4].strip()], sep="")