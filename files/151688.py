pet_codes = {"Dog": 0, "Cat": 1, "Fish": 2}
pets = [pet.strip() for pet in input("Enter your pets: ").split(",")]
codes = [str(pet_codes[pet]) for pet in pets]
print("Code of your pets:", ",".join(codes))