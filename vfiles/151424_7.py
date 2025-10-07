animal_list = {"Dog":0,"Cat": 1,"Dog": 0,"Fish": 2,"Cat": 1}

animal = "Dog,Cat,Dog,Fish,Cat"
animal = animal.split(",")
print('Enter your pets:',end='')
print("Dog,Cat,Dog,Fish,Cat",sep=',')
print('Code of your pets:',end='')
print(animal_list[animal[0]],animal_list[animal[1]],animal_list[animal[0]],animal_list[animal[2]],animal_list[animal[1]],sep=',')