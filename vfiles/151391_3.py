pet_code = {"Dog": 0,"Cat": 1,"Fish": 2}

one_hot = {"Dog": [1, 0, 0],"Cat": [0, 1, 0],"Fish": [0, 0, 1]}

input_str = input("Enter your pets: ")

pets = input_str.split(",")

pet0 = pets[0].strip()
pet1 = pets[1].strip()
pet2 = pets[2].strip()
pet3 = pets[3].strip()
pet4 = pets[4].strip()

print(”Code of your pets:", 
      pet_code[pet0], ",", 
      pet_code[pet1], ",", 
      pet_code[pet2], ",", 
      pet_code[pet3], ",", 
      pet_code[pet4], sep=" ")

print("One-hot vectors:")
print(one_hot[pet0])
print(one_hot[pet1])
print(one_hot[pet2])
print(one_hot[pet3])
print(one_hot[pet4])