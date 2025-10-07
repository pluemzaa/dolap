n1 = input(”Enter your pets: “)
n5 = n1.split(”,“)
nIl = {”Dog“: 0, ”Cat“: 1,”Fish“: 2}
print(”Code of your pets: “, end= ” “)
print(nIl[n5[0]],nIl[n5[1]],nIl[n5[2]],nIl[n5[3]],nIl[n5[4]],sep=”,“)