one_hot = {
    "Dog":  [1, 0, 0],
    "Cat":  [0, 1, 0],
    "Fish": [0, 0, 1]
}
text = input("Enter your pets: ")

code_dict = {
    "Dog": 0,
    "Cat": 1,
    "Fish": 2
}

onehot_list = [
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1]
]

text = input("Enter your pets: ")

pets = text.split(",")

c0 = code_dict[pets[0]]
c1 = code_dict[pets[1]]
c2 = code_dict[pets[2]]
c3 = code_dict[pets[3]]
c4 = code_dict[pets[4]]

print("Code of your pets:", str(c0) + "," + str(c1) + "," + str(c2) + "," + str(c3) + "," + str(c4))
print("One-hot vectors:")
print(onehot_list[c0])
print(onehot_list[c1])
print(onehot_list[c2])
print(onehot_list[c3])
print(onehot_list[c4])