pet = {"Dog": [0], "Cat": [1], "Fish": [2]}
petcode = {"Dog": [1, 0, 0],"Cat": [0, 1, 0],"Fish": [0, 0, 1]}

x = input("Enter your pets: ")
xp = x.split(",")

xp = [xp.strip().title() for xp in xp]

print("Code of your pets: ", end=" ")
print(pet[xp[0]][0], ",", pet[xp[1]][0], ",", pet[xp[2]][0], ",", pet[xp[3]][0], ",", pet[xp[4]][0], sep="")

print("One-hot vectors:")
print(petcode[xp[0]])
print(petcode[xp[1]])
print(petcode[xp[2]])
print(petcode[xp[3]])
print(petcode[xp[4]])