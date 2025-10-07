pet_to_code = {"Dog": 0,"Cat": 1,"Fish": 2}
one_hot = {
    0: [1, 0, 0],  # Dog
    1: [0, 1, 0],  # Cat
    2: [0, 0, 1]   # Fish}
user_input = input("Enter your pets: ")
pet_list = [pet.strip() for pet in user_input.split(",")]
code_list = [pet_to_code[pet] for pet in pet_list]
print("Code of your pets:", ",".join(str(code) for code in code_list))
print("One-hot vectors:")
for code in code_list:
    print(one_hot[code])