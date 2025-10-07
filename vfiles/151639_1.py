input_hex = "DOG,CAT,FISH"
hexs = input_hex.split(",")
print(hexs[0])
haxs_dict = {"DOG":0, "CAT":1, "FISH":2}
print(hex_dict[hexs[0]],
      hex_dict[hexs[1]],
      hex_dict[hexs[2]],sep=',')