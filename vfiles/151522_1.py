animal_codes = {
    "Dog": 0,
    "Cat": 1,
    "Fish": 2
}
one_hot_vectors = {
    "Dog": [1, 0, 0],
    "Cat": [0, 1, 0],
    "Fish": [0, 0, 1]
}
pets_input = input("Enter your pets (comma-separated, 5 names): ")


pets_list = [pet.strip() for pet in pets_input.split(',')]

if len(pets_list) != 5:
    print("Error: Please enter exactly 5 pet names.")
else:
    coded_pets = []
    vectors_output = []
    for pet in pets_list:
        if pet in animal_codes:
            coded_pets.append(str(animal_codes[pet])) # แปลงเป็น string เพื่อรวมในผลลัพธ์
            vectors_output.append(one_hot_vectors[pet])
        else:
            print(f"Warning: '{pet}' is not a recognized pet type. Skipping.")
            coded_pets.append("N/A") 
            vectors_output.append("N/A")
    print("Code of your pets: " + ",".join(coded_pets))
    print("One-hot vectors:")
    for vector in vectors_output:
        print(vector)