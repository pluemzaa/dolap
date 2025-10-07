pet_codes = {"Dog": 0,"Cat": 1,"Fish": 2}

input_str = input("Enter your pets: ")

pets = [pet.strip() for pet in input_str.split(',')]

if len(pets) != 5:
    print("Error: Please enter exactly 5 pet names.")
else:
    codes = [str(pet_codes[pet]) for pet in pets]
    
    print("Code of your pets:", ",".join(codes))