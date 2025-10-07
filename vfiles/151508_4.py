def generate_one_hot_vectors():
    pet_mapping = {
        "Dog": {"code": "0", "vector": [1, 0, 0]},
        "Cat": {"code": "1", "vector": [0, 1, 0]},
        "Fish": {"code": "2", "vector": [0, 0, 1]}
    }

    user_input = input("Enter your pets: ")
    pets_list = [pet.strip() for pet in user_input.split(',')]

    encoded_codes = []
    one_hot_vectors_output = []

    for pet in pets_list:
        if pet in pet_mapping:
            encoded_codes.append(pet_mapping[pet]["code"])
            vector_str = str(pet_mapping[pet]["vector"]).replace("[", "").replace("]", "")
            one_hot_vectors_output.append(vector_str)

    print("Code of your pets: " + ",".join(encoded_codes))
    print("One-hot vectors:")
    for vector_str in one_hot_vectors_output:
        print(vector_str)

generate_one_hot_vectors()