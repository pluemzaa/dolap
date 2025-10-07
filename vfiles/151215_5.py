a = {"Dog":0,"Cat":1,"Fish":2}
b_str = input("Enter your pets:")
b = b_str.split(",")
print("Code of your pets:",end="")
print(a[b[0]],a[b[1]],a[b[2]],a[b[3]],a[b[3]],sep=",")