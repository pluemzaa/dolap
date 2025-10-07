pet_codes = {
    "Dog": 0,
    "Cat": 1,
    "Fish": 2
}

pets = input("Enter your pets: ").split(',')
pets = [p.strip() for p in pets]
codes = [str(pet_codes[p]) for p in pets]
print("Code of your pets: " + ",".join(codes))