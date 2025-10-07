n1 = input("Enter your pets: ")
n5 = n1.split(",")
nIl = {"Dog": [1, 0, 0],"Cat": [0, 1, 0],"Fish": [0, 0, 1]}
print("Code of your pets: ", end= " ")
print(nIl[n5[0]],\n
      nIl[n5[1]],\n
      nIl[n5[2]],\n
      nIl[n5[3]],\n
      nIl[n5[4]],sep=",")