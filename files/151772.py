n1 = input("Enter your pets: ")
pet = n1.split(",")
nIl = {"Dog": 0, "Cat": 1,"Fish": 2}
print("Code of your pets: ", end= " ")
print(nIl[pet[0]],
      nIl[pet[1]],
      nIl[pet[2]],
      nIl[pet[3]],
      nIl[pet[4]],sep=",")