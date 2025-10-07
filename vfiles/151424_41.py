animal_dict = input("Enter your pets: ")
animal_dict = {"Dog":[0], "Cat":[1], "Fish":[2]}

animal = "Dog,Cat,Dog,Fish,Cat"
animal = animal.split(",")
print("Code of your pets:", end='')
print(animal_dict[animal[0]],animal_dict[animal[1]],animal_dict[animal[2]],animal_dict[animal[3]],animal_dict[animal[4]],sep=",")