n1 = input("Enter your pets: ")
n5 = n1.split(",")
nIl = {"Dog": [1, 0, 0],"Cat": [0, 1, 0],"Fish": [0, 0, 1]}
print("Code of your pets: ", end= " ")
print(nIl[n5[0]],
      nIl[n5[1]],
      nIl[n5[2]],
      nIl[n5[3]],
      nIl[n5[4]],sep=",")