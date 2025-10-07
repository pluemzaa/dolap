num_dict = {'Dog': 0,'Cat' : 1 ,'Fish' : 2}
pet = input('Enter your pets: ')
hex_str = (pet)
hex_num = hex_str.split(" , ")
print ("Code of your pets: ",end = ' ')
print(num_dict[hex_num[0]] , num_dict[hex_num[1]] , num_dict[hex_num[2]],num_dict[hex_num[3]] , num_dict[hex_num[4]],sep=',')