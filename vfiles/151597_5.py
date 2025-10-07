input_hex="Dog,Cat,Dog,Fish,Cat" #output:10,10,15,15
hexs=input_hex.split(",")
print(hexs)
hex_dict={"Dog":0,"Cat":1,"Fish":2}
print("Code of your pets:", end=" ")
print(hex_dict[hexs[0]],
      hex_dict[hexs[1]],
      hex_dict[hexs[2]],
      hex_dict[hexs[3]],
      hex_dict[hexs[4]],sep=',')