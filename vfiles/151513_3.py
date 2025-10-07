num_dict = {"Dog":[1,0,0],"Cat":[0,1,0],"Fish":[0,0,1]}
hex_str = input("Enter your pets:")
hex_num = hex_str.split(",")
print("One-hot vectors:", end='\n')
print(num_dict[hex_num[0]],
num_dict[hex_num[1]],
num_dict[hex_num[2]],
num_dict[hex_num[3]], sep= '\n')