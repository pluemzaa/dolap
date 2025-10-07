pet_dict={"Dog":0,
          "Cat":1,
          "Fish":2}

pets=input("Enter your pets: ")
pets1_List=pets.split(',')
pets_code_List=[
    str(pet_dict[pets1_List[0]]),
    str(pet_dict[pets1_List[1]]),
    str(pet_dict[pets1_List[2]]),
    str(pet_dict[pets1_List[3]]),
    str(pet_dict[pets1_List[4]])]

print("Code of your pets:",
      pets_code_List[0],
      pets_code_List[1],
      pets_code_List[2],
      pets_code_List[3],
      pets_code_List[4],
      sep=',')