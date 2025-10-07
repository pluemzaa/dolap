input_1 = input("Enter your pets: ")
split_ = input_1.split(",")
dict_ = {"Dog": 0, "Cat": 1, "Fish": 2}

print("Code of your pets:", dict_[split_[0]], dict_[split_[1]], dict_[split_[2]], sep=",")

print("One-hot vectors: ")
dict1 = {"Dog": [1, 0, 0], "Cat": [0, 1, 0], "Fish": [0, 0, 1]}
for something in split_:
    gg = dict1.get(something)
    print(gg)