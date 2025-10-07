pet_to_code_map = {"Dog": 0, "Cat": 1, "Fish": 2}
recieve_type = input("Enter your pets, separated by commas: ")
name_list = recieve_type.split(',')
code_list = []

for name in name_list:
  code_list.append(pet_to_code_map[name])

print(f"Code of your pets: {code_list}")