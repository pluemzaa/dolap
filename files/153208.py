# Create a dictionary to store pet codes
pet_codes = {
    "Dog": "0",
    "Cat": "1",
    "Fish": "2"
}
# Get input from the user
pets_input = input("Enter your pets: ")
# Split the input into a list
pets_list = pets_input.split(',')
# Create a list to store the codes
code_list = []
# Convert each pet name to its code
for pet in pets_list:
    code = pet_codes[pet]
    code_list.append(code)
# Show the result
print("Code of your pets:", ",".join(code_list))