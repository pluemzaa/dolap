a = {"Dog":0,"Cat":1,"Fish":2}
a2 = {"Dog":[1, 0, 0],"Cat":[0, 1, 0],"Fish":[0, 0, 1]}
b_str = input("Enter your pets:")
b = b_str.split(",")
print("Code of your pets:",end="")
print(a[b[0]],a[b[1]],a[b[2]],a[b[3]],a[b[4]],sep=",")
print("One-hot vectors:",end="\n")
print(a2[b[0]],a2[b[1]],a2[b[2]],a2[b[3]],a2[b[4]],sep="\n")