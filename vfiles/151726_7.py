pet_codes = {"Dog": 0,"Cat": 1,"Fish": 2}
one_hot_vectors = {"Dog": [1, 0, 0],"Cat": [0, 1, 0],"Fish": [0, 0, 1]}
input_pets = input("Enter your pets: ")
pets = input_pets.split(',')
encoded_pets = list(map(get_pet_code, pets))
print("Code of your pets:", ",".join(map(str, encoded_pets)))
print("One-hot vectors:")
one_hot_vectors_list = list(map(get_one_hot_vector, pets))
print("\n".join(map(str, one_hot_vectors_list)))