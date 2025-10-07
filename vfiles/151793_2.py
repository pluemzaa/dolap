num_dict = {"Dog": [0], "Cat": [1], "Fish": [2]}
animals = input("Enter your pets: ")
hex_str = "Dog,Cat,Fish"
hex_num = hex_str.split(",")
print("Code of your pets: ", end=' ')
print(num_dict[hex_num[0]],
      num_dict[hex_num[1]],
      num_dict[hex_num[2]],sep=',')