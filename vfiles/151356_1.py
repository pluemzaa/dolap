pet_to_code = {"Dog": 0, "Cat": 1, "Fish": 2}

code_to_onehot = {0: [1, 0, 0], 1: [0, 1, 0], 2: [0, 0, 1]}

input_text = input("Enter your pets: ")
input_list = input_text.split(',')

print("Code of your pets:", end=' ')
print("One-hot vectors:")