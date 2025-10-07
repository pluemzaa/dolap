pet_codes = {
    "Dog": 0,
    "Cat": 1,
    "Fish": 2
}
text = input("Enter your pets: ")
pets = text.split(",")
codes = [
    str(pet_codes[pets[0]]),
    str(pet_codes[pets[1]]),
    str(pet_codes[pets[2]]),
    str(pet_codes[pets[3]]),
    str(pet_codes[pets[4]])
]
print("Code of your pets:", codes[0] + "," + codes[1] + "," + codes[2] + "," + codes[3] + "," + codes[4])

pet_codes2 = {
    "Dog": [1,0,0],
    "Cat": [0,1,0],
    "Fish": [0,0,1]
}
codes2 = [
    str(pet_codes2[pets[0]]),
    str(pet_codes2[pets[1]]),
    str(pet_codes2[pets[2]]),
    str(pet_codes2[pets[3]]),
    str(pet_codes2[pets[4]])
]
print("One-hot vectors:", codes2[0] ,",", codes2[1] , "," , codes2[2] ,"," , codes2[3] , "," , codes2[4])