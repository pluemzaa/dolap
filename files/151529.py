pet_codes = {"Dog": 0,"Cat": 1,"Fish": 2}

one_hot_vectors = {"Dog": [1, 0, 0],"Cat": [0, 1, 0],"Fish": [0, 0, 1]}

pets_input = input("Enter your pets: ")
pets_list = pets_input.split(",")

if len(pets_list) != 5:
    print("Please enter exactly 5 pet names separated by commas.")
else:
    codes = []
    one_hots = []

    for pet in pets_list:
        pet = pet.strip()

        if pet in pet_codes:
            codes.append(str(pet_codes[pet]))
            one_hots.append(one_hot_vectors[pet])
        else:
            codes.append("?")
            one_hots.append(["?", "?", "?"])

  
    print("Code of your pets:", ",".join(codes))

    print("one_hot_vectors")
    for vec in one_hots:
        print(vec)