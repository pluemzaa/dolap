animal_str = input("Enter your pets:")
animal_str = {"Dog":[0],"Cat":[1],"Fish":[2]}

animal = "Dog,Cat,Dog,Fish,Cat"
animal = animal.split(",")
print('Result:',end='')
print(animal_str[animal[0]],animal_str[animal[1]],animal_str[animal[2]],sep=',')