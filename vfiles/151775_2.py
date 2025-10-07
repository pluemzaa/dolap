pets_dict = {
    "Dog": 0,
    "Cat": 1,
    "Fish": 2
}
one_hot_list = [
    [1, 0, 0],  # Dog
    [0, 1, 0],  # Cat
    [0, 0, 1]   # Fish
]

pets_input = input("Enter your pets: ")
pets_list = pets_input.split(",")
codes = [pets_dict[pet] for pet in pets_list]
print("code of your pets:", ",".join(map(str, codes)))
print("cne-hot vectors:")
for code in codes:
    print(one_hot_list[code])