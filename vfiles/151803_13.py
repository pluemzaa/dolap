animal = {
    "Dog": 0, 
    "Cat": 1,
    "Fish": 2 }
animal_input = input("enter your pets: ")
print_split= animal_input.split(',')

animal_code =( 
            animal[print_split[0]],
            animal[print_split[1]],
            animal[print_split[2]],
            animal[print_split[3]],
            animal[print_split[4]] )

print ("Code of your pets: ", animal_code)