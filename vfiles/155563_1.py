input_1 = input("Enter your pets: ")
split_ = input_1.split(",")

dict1 = {"Dog": 0, "Cat": 1, "Fish": 2}

print("Code of your pets:", end=" ")
print(dict1[split_[0].strip()], dict1[split_[1].strip()], dict1[split_[2].strip()],
      dict1[split_[3].strip()], dict1[split_[4].strip()], sep=”,“)
print("One-hot vectors:")

dict2 = {"Dog": [1, 0, 0], "Cat": [0, 1, 0], "Fish": [0, 0, 1]}
for something in split_:
    gg = dict2.get(something.strip())
    print(gg)