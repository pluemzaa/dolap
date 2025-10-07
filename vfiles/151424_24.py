animal_intput=input("Enter your pets:")
animal_dict={"Dog":0, "Cat":1, "Fish":2}

animal="Dog,Cat,Dog,Fish,Cat"
animal=animal.split(",")
print("Code of your pets:",end='')
print(animal_dict[animal[0].strip()],animal_dict[animal[1].strip()],animal_dict[animal[2].strip()],animal_dict[animal[3].strip()],animal_dict[animal[4].strip()],sep=",")