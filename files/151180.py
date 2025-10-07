Pet = {"Dog":0,"Cat":1,"Fish":2}
Petvectors = {"Dog":[1, 0, 0],"Cat":[0, 1, 0],"Fish":[0, 0, 1]}
Pet_str = input("Enter your pets:")
b = Pet_str.split(",")
print("Code of your pets:",end="")
print(Pet[b[0]],Pet[b[1]],Pet[b[2]],Pet[b[3]],Pet[b[4]],sep=",")
print("One-hot vectors:",end="\n")
print(Petvectors[b[0]],Petvectors[b[1]],Petvectors[b[2]],Petvectors[b[3]],Petvectors[b[4]],sep="\n")