animal = {
    "Dog": 0,
    "Cat": 1,
    "Fish": 2
}

animal_input = input("Enter your pets: ")  
print_split = animal_input.split(',')

print0 = print_split[0].strip()
print1 = print_split[1].strip()
print2 = print_split[2].strip()
print3 = print_split[3].strip()
print4 = print_split[4].strip()

code0 = str(animal[print0])
code1 = str(animal[print1])
code2 = str(animal[print2])
code3 = str(animal[print3])
code4 = str(animal[print4])

print("Code of your pets:", ([code0, code1, code2, code3, code4]))