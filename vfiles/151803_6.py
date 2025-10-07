animal = {
    "Dog": 0, 
    "Cat": 1,
    "Fish": 2}
animal_name = input("enter your pets: ")
print_split= print_inputl.split(',')

animal_code =( animal[animal_name[0]],
                     animal[animal_name[1]],
                     animal[animal_name[2]],
                     animal[animal_name[3]],
                     animal[animal_name[4]] )

print ("Code of your pets: ", animal_code)