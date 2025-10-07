num_dict ={"Dog": 0,"Cat":1,"Fish":2}
One_hot_vector = {"Dog": [1, 0, 0],"Cat":	[0, 1, 0],"Fish":	[0, 0, 1]}
P = input("Enter your pets:")

num_dict1 = P.split(",")

print("Code of your pets:",num_dict[num_dict1[0]],',',num_dict[num_dict1[1]],',',num_dict[num_dict1[2]],',',num_dict[num_dict1[3]],',',num_dict[num_dict1[4]])
print("One-hot vectors:\n",One_hot_vector[num_dict1[0]],'\n',One_hot_vector[num_dict1[1]],'\n',One_hot_vector[num_dict1[2]],'\n',One_hot_vector[num_dict1[3]],'\n',One_hot_vector[num_dict1[4]])