def generate_one_hot_vectors_shortest():
    pet_mapping = {
        "Dog": {"code": "0", "vector": [1, 0, 0]},
        "Cat": {"code": "1", "vector": [0, 1, 0]},
        "Fish": {"code": "2", "vector": [0, 0, 1]}
    }

    user_pets = [p.strip() for p in input("Enter your pets: ").split(',')]

    encoded_codes = [pet_mapping[p]["code"] for p in user_pets if p in pet_mapping]
    one_hot_vectors = [str(pet_mapping[p]["vector"]).replace("[", "").replace("]", "") for p in user_pets if p in pet_mapping]

    print(f"Code of your pets: {','.join(encoded_codes)}")
    print("One-hot vectors:")
    print('\n'.join(one_hot_vectors))

generate_one_hot_vectors_shortest()