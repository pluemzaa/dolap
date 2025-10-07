dict_ = {"Dog":0,"Cat":1,"Fish":2}
dict_2 = {"Dog":[1, 0, 0],"Cat":[0, 1, 0],"Fish":[0, 0, 1]}
x = input("Enter your pets: ").split(",")
print(f"Code of your pets: {dict_[x[0]]},{dict_[x[1]]},{dict_[x[2]]},{dict_[x[3]]},{dict_[x[4]]}")
print("One-hot vectors:",dict_2[x[0]],dict_2[x[1]],dict_2[x[2]],dict_2[x[3]],dict_2[x[4]],sep="\n")