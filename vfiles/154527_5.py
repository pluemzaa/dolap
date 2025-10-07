pet_codes = {"Dog": 0,"Cat": 1,"Fish": 2}

user_input = input("Enter your pets: ")

pet_list = user_input.split(',')

code_list = []

for pet_name in pet_list:
    code = pet_codes[pet_name]
    code_list(code)

string_codes = [str(c) for c in code_list]

result = ",".join(string_codes)

print(f"Code of your pets: {result}")