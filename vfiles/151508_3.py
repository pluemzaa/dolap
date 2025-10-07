def generate_one_hot_vectors():
    one_hot_map = {
        "Dog": [1, 0, 0],
        "Cat": [0, 1, 0],
        "Fish": [0, 0, 1]
    }

    user_input = input("Enter your pets: ")
    pets_list = [pet.strip() for pet in user_input.split(',')]

    encoded_codes = []
    one_hot_vectors_output = []

    for pet in pets_list:
        if pet == "Dog":
            encoded_codes.append("0")
        elif pet == "Cat":
            encoded_codes.append("1")
        elif pet == "Fish":
            encoded_codes.append("2")
        
        if pet in one_hot_map:
            one_hot_vectors_output.append(str(one_hot_map[pet]))

    print("Code of your pets: " + ",".join(encoded_codes))
    print("One-hot vectors:")
    for vector in one_hot_vectors_output:
        print(vector.replace("[", "").replace("]", ""))

generate_one_hot_vectors()