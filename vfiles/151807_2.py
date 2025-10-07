input_hex = input("Enter your pet: ")
hexs=input_hex.split(",")
print(hexs)
hex_dict = {"Dog":0, "Cat": 1,"Fish": 2}
print("Code of your pets: ", end= " ")
print(hex_dict[hex[0]],
      hex_dict[hex[1]],
      hex_dict[hex[2]],
      hex_dict[hex[3]],
      hex_dict[hex[4]],sep=',')