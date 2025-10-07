num_dict = {"Dog": 0, "Cat": 1, "Fish": 2}
hot_dict = {"Dog": [1,1,0], "Cat": [0,1,0], "Fish": [0,0,1]}
animal_str = input("Enter your pets: ")
hex_num = animal_str.split(",")
print("Code of your pets:", end=' ')
print(num_dict[hex_num[0]],
      num_dict[hex_num[1]],
      num_dict[hex_num[2]],
       num_dict[hex_num[3]],
        num_dict[hex_num[4]],
      sep=',')

print("One-hot vectors: ",end='\n')
print(hot_dict[hex_num[0]],
      hot_dict[hex_num[1]],
      hot_dict[hex_num[2]],
      hot_dict[hex_num[3]],
      hot_dict[hex_num[4]],
      sep='\n')