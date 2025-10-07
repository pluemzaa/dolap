input_hex = "Dog,Cat,Fish"
hexs = input_hex.split(",")
print(hexs[0])
hex_dict = {"Dog":0,"Cat":1,"Fish":2}
print("Enter your pets:", end="")
print(hex_dict[hexs[0]],
      hex_dict[hexs[1]],
      hex_dict[hexs[2]],sep=',')