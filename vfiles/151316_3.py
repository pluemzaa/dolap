pet_to_code = {
    "Dog": 0,
    "Cat": 1,
    "Fish": 2
}

one_hot = [
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1]
]

text = input("Enter your pets: ")

print("Enter your pets:", text)

pets = text.split(",")

code0 = pet_to_code[pets[0]]
code1 = pet_to_code[pets[1]]
code2 = pet_to_code[pets[2]]
code3 = pet_to_code[pets[3]]
code4 = pet_to_code[pets[4]]

print("Code of your pets:", f"{code0},{code1},{code2},{code3},{code4}")

print("One-hot vectors:")
print(one_hot[code0])
print(one_hot[code1])
print(one_hot[code2])
print(one_hot[code3])
print(one_hot[code4])