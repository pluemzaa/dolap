input_1 = input("Enter your pets: ")
split_ = input_1.split(",")
dict_ = {"Dog": 0, "Cat": 1, "Fish": 2}

print("Code of your pets:", end=' ')
print(dict_[split_[0]], dict_[split_[1]], dict_[split_[2]],dict_[split_[3]],dict_[split_[4]], sep=",")



dict1 = {"Dog": [1, 0, 0], "Cat": [0, 1, 0], "Fish": [0, 0, 1]}

print(“One-hot vectors: “ , end=‘\n’)
print(dict1[split_[0]],
dict1[split_[1]],
dict1[split_[2]],
dict1[split_[3]],
dict1[split_[4]],
sep=“\n”)