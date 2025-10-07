pet_codes = {"Dog": 0,"Cat": 1,"Fish": 2 }

input_str = input("Enter your pets (separated by ','): ")

pets = input_str.split(',')

else:
    codes = [str(pet_codes[pet.strip()]) for pet in pets]
    print("Code of your pets:", ",".join(codes))