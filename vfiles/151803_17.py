animal= {
    "Dog": 0,
    "Cat": 1,
    "Fish": 2
}

animal_input = input("enter your pets: ")
print_split = animal_input.split(',')

animal_code = (
    animal[print_split[0].strip().title()],
    animal[print_split[1].strip().title()],
    animal[print_split[2].strip().title()],
    animal[print_split[3].strip().title()],
    animal[print_split[4].strip().title()]
)

print("Code of your pets: ", animal_code)