animals = {"Dog": [0], "Cat": [1], "Fish": [2]}
kodron = {
    "Dog": [1, 0, 0],
    "Cat": [0, 1, 0],
    "Fish": [0, 0, 1]
}

x = input("Enter your pets: ")
x2 = x.split(",")

x2 = [pet.strip().title() for pet in p]

print("Code of your pets: ", end="")
print(
    animals[x2[0]][0], ",",
    animals[x2[1]][0], ",",
    animals[x2[2]][0], ",",
    animals[x2[3]][0], ",",
    animals[x2[4]][0], sep=","
)

print("One-hot vectors:")
print(kodron[x2[0]])
print(kodron[x2[1]])
print(kodron[x2[0]])
print(kodron[x2[1]])