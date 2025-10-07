num_dict = {"Dog": 0, "Cat": 1, "Fish": 2}
num_dict1 = {"Dog": [1,0,0], "Cat": [0,1,0], "Fish": [0,0,1]}
hex_str = input ("Enter your pets:")
hex_num = hex_str.split(",")
print("Code of your pets:", end=' ')
print(num_dict[hex_num[0]],
      num_dict[hex_num[1]],
      num_dict[hex_num[2]],
      num_dict[hex_num[3]],
      num_dict[hex_num[4]],sep=",")
hex_num1 = hex_str.split(",")
print("One-hot vectors:", end='\n')
print(num_dict1[hex_num1[0]],
      num_dict1[hex_num1[1]],
      num_dict1[hex_num1[2]],
      num_dict1[hex_num1[3]],
      num_dict1[hex_num1[4]],sep="\n")