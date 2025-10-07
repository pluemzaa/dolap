input_hex = input("Enter your pets: ")
hexs = input_hex.split(",")
print(hexs)
hex_dict = {"Dog":[1,0,0],
            "Cat":[0,1,0],
            "Fish":[0,0,1]}
print("Code of your pets: ", end= " ")
print(hex_dict[hexs[0]],
      hex_dict[hexs[1]],
      hex_dict[hexs[2]],
      hex_dict[hexs[3]],
      hex_dict[hexs[4]],sep=',')
print("One-hot vectors:", end="\n")
print(hex_dict[hexs[0]],
      hex_dict[hexs[1]],
      hex_dict[hexs[2]],
      hex_dict[hexs[3]],
      hex_dict[hexs[4]],sep='\n')