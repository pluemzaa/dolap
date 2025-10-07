pet_codes = {
    "Dog": 0,
    "Cat": 1,
    "Fish": 2
}
text = input("Enter your pets: ")
pets = text.split(",")
codes = [
    str(pet_codes[pets[0]]),
    str(pet_codes[pets[1]]),
    str(pet_codes[pets[2]]),
    str(pet_codes[pets[3]]),
    str(pet_codes[pets[4]])
]
print("Code of your pets:", codes[0] + "," + codes[1] + "," + codes[2] + "," + codes[3] + "," + codes[4])