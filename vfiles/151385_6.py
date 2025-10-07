pet_code = {”Dog“: 0,”Cat“: 1,”Fish“: 2}

input_str = input(”Enter your pets: “)

pets = input_str.split(”,“)

pet0 = pet_code[pets[0].strip()]
pet1 = pet_code[pets[1].strip()]
pet2 = pet_code[pets[2].strip()]
pet3 = pet_code[pets[3].strip()]
pet4 = pet_code[pets[4].strip()]
pet5 = pet_code[pets[5].strip()]

print(”Code of your pets:“, pet0, ”,“, pet1, ”,“, pet2, ”,“, pet3, ”,“, pet4, ”,“, sep=”“)