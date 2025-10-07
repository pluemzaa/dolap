n1 = input("Enter your pets: ")
n5 = n1.split(",")
nll = {"Dog": 0, "Cat": 1,"Fish": 2}
print("Code of your pets: ", end= " ")
print(nll[n5[0]],
      nll[n5[1]],
      nll[n5[2]],
      nll[n5[3]],
      nll[n5[4]],)