A = input("Enter your pets")
hex_dict = {"Dog":0,"Cat":1,"Fish":2}
p = A.split(",")
print("Code of your pets", end="")
print(hex_dict[p[0]],
	hex_dict[p[1]],
	hex_dict[p[2]],
	hex_dict[p[3]],
	hex_dict[p[4]],sep=','