num_dict = {"Dog": 0, "Cat": 1, "Fish": 2}
animal_str = input("Enter your pets: ")
hex_num = animal_str.split(",")
print("Code of your pets:",num_dict[hex_num[0]],
      num_dict[hex_num[1]],
      num_dict[hex_num[2]],
      num_dict[hex_num[3]],
      num_dict[hex_num[4]],
      sep=',')