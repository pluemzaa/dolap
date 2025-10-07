pet_name = {"Dog": 0, "Cat": 1, "Fish": 2}
pet_str = input("Enter your pets: ")
pets = [pet.strip().title() for pet in pet_str.split(',')]


if len(pets) != 5:
    print("Error: Please enter exactly 5 pet names.")

else:
    codes = [pet_name[pet] for pet in pets]

    print("Code of your pets:", ",".join(map(str, codes)))