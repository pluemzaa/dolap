#Dog = 0
#Cat = 1
#Fish= 2
Pet = {"Dog":0,"Cat":1,"Fish":2}
b_str = input("Enter your pets:")
b = b_str.split(",")
print("Code of your pets:",end="")
print(Pet[b[0]],Pet[b[1]],Pet[b[2]],Pet[b[3]],Pet[b[4]],sep=",")