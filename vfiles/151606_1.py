hyu = input("Enter your pets: ")
huu = hyu.split(",")
ggex = {"Dog": 0, "Cat": 1,"Fish": 2}
print("Code of your pets:", end=" ")
print(ggex[huu[0]],
      ggex[huu[1]],
      ggex[huu[2]],
      ggex[huu[3]],
      ggex[huu[3]],sep=',')