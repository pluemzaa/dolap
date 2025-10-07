def generate_one_hot():
    pet_names = ['Dog', 'Cat', 'Fish']
    pets_input = input("Enter your pets: ")
    pets = pets_input.split(',')

    pet_codes = [pet_names.index(pet) for pet in pets]
    print(f"Code of your pets: {','.join(map(str, pet_codes))}")
    
    print("One-hot vectors:")
    for code in pet_codes:
        one_hot = [0] * 3
        one_hot[code] = 1
        print(one_hot)

generate_one_hot()