pet_to_code = {'Dog': 0, 'Cat': 1, 'Fish': 2}
code_to_vector = {0: [1, 0, 0],1: [0, 1, 0],2: [0, 0, 1]}

pets = input("Enter your pets: ").split(',')
codes = list(map(lambda pet: pet_to_code[pet.strip()], pets))
vectors = list(map(lambda code: code_to_vector[code], codes))

print("Code of your pets:", ','.join(map(str, codes)))
print("One-hot vectors:")
print('\n'.join(map(str, vectors)))