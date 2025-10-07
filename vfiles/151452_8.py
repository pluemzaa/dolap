num_dict = {"Dog": 0, "Cat": 1,"Fish": 2}
hnum = input("Enter your pets: ")
hnum = hnum.split(",")
print('Code of your pets: ',end=' ')
print(num_dict[hnum[0]],num_dict[hnum[1]],num_dict[hnum[2]],num_dict[hnum[3]],num_dict[hnum[4]])