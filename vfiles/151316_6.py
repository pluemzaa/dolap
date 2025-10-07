pets = ['Dog', 'Cat', 'Fish']
vectors = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

pet = input("Enter your pet: ")
index = 0 * (pet == 'Dog') + 1 * (pet == 'Cat') + 2 * (pet == 'Fish')
one_hot = vectors[index]

print("Code of your pet:", index)
print("One-hot vector:", one_hot)