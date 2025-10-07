pet_codes = {"Dog": 0,"Cat": 1,"Fish": 2}
pets_input = input("Enter your pets: ")
pets_list = pets_input.split(',')
if len(pets_list) != 5:
print("You must enter exactly 5 pet names separated by commas.")
else:
codes = []
for pet in pets_list:
pet = pet.strip()  
if pet in pet_codes:
codes.append(str(pet_codes[pet]))
else:
print(f"Unknown pet: {pet}")
break else:
print("Code of your pets:", ','.join(codes))