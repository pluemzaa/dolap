A = input("Enter your pets: ")
hex_dict = {"Dog":[1,0,0],"Cat":[0,1,0],"Fish":[0,0,1]}
p = A.split(",")
hex_dicE = {"Dog":0,"Cat":1,"Fish":2}
print("Code of your pets: ", end=",")
print(hex_dicE[p[0]],
	hex_dicE[p[1]],
	hex_dicE[p[2]],
	hex_dicE[p[3]],
	hex_dicE[p[4]],sep=',')
print ("One-hot vectors:",end="\n")
print(hex_dict[p[0]],
	hex_dict[p[1]],
	hex_dict[p[2]],
	hex_dict[p[3]],
	hex_dict[p[4]],sep='\n')