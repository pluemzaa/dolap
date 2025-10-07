pet_code = {"Dog": [0], "Cat": [1], "Fish": [2]}
one_hot = {
    "Dog": [1, 0, 0],
    "Cat": [0, 1, 0],
    "Fish": [0, 0, 1]
}

pet_text = input("Enter your pets: ")
p = pet_text.split(",")

p = [pet.strip().title() for pet in p]

print("Code of your pets: ", end="")
print(
    pet_code[p[0]][0], ",",
    pet_code[p[1]][0], ",",
    pet_code[p[2]][0], ",",
    pet_code[p[3]][0], ",",
    pet_code[p[4]][0], sep=""
)

print("One-hot vectors:")
print(one_hot[p[0]])
print(one_hot[p[1]])
print(one_hot[p[2]])
print(one_hot[p[3]])
print(one_hot[p[4]])