num_dict = {"A": [1, 0, 0], "B": [0, 1, 0], "C": [0, 0, 1]}
hex_str = input("Enter hex code (space-separated): ")
hex_num = hex_str.split(",")
print("Result:" , end='\n')
print(num_dict[hex_num[0]],
num_dict[hex_num[1]],
num_dict[hex_num[2]],
num_dict[hex_num[3]],sep="\n")