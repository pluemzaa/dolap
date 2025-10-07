animal_text = {"Dog":0,"Cat": 1,"Dog": 0,"Fish": 2,"Cat": 1}

animal = "Dog,Cat,Dog,Fish,Cat"
animal = animal.split(",")
print('Enter your pets:',end='')
print("Dog,Cat,Dog,Fish,Cat",sep=',')
print('Code of your pets:',end='')
print(animal_text[animal[0]],animal_text[animal[1]],animal_text[animal[0]],animal_text[animal[2]],animal_text[animal[1]],sep=',')