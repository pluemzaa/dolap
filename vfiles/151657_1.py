pet_codes = {
    "Dog": "0",
    "Cat": "1",
    "Fish": "2"
}
user_input = input("Enter your pets: ").strip()
pet_list = user_input.split(',')
encoded_codes = []
for pet in pet_list:
      clean_pet_name = pet.strip() 
code = pet_codes[clean_pet_name]
encoded_codes.append(code)
output_string = ",".join(encoded_codes)
print(f"Code of your pets: {output_string}")