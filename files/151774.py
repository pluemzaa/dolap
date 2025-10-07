pets_input = input("Enter your pets: ")

animal_dict = {"Dog": 0, "Cat": 1, "Fish": 2}

pets_list = pets_input.split(",")

codes = [animal_dict[pet] for pet in pets_list]

print("code of your pets:", ",".join(map(str, codes)))