num_dict = {"Dog": 0, "Cat": 1,"Fish": 2}
hnum = input("Enter your pets:")
hnum = hnum.split(",")
print('Code of your pets:',end=' ')
print(num_dict[hnum[0]],num_dict[hnum[1]],num_dict[hnum[2]],num_dict[hnum[3]],num_dict[hnum[4]],sep=",")
num_dict = {"Dog": [1,0,0], "Cat": [0,1,0],"Fish": [0,0,1]}
print("One-hot vectors:",end='\n')
print(num_dict[hnum[0]],num_dict[hnum[1]],num_dict[hnum[2]],num_dict[hnum[3]],num_dict[hnum[4]],sep='\n')