n1 = input("Enter your pets: ")
n5 = n1.split(",")
ggex = {"Dog": 0, "Cat": 1,"Fish": 2}
print("Code of your pets:", end=" ")
print(ggex[n5[0]],
      ggex[n5[1]],
      ggex[n5[2]],
      ggex[n5[3]],
      ggex[n5[4]],sep=',')