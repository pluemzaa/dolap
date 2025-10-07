hyu = input("Enter your pets: ")
huu = hyu.split(",")
ggex = {"Dog": 0, "Cat": 1,"Fish": 2}
print("Code of your pets:",ggex[huu[0]],ggex[huu[1]],ggex[huu[2]],ggex[huu[3]],ggex[huu[4]],sep=',')

print("One-hot vectors:")
ggey = {"Dog": [1, 0, 0], "Cat": [0, 1, 0],"Fish": [0, 0, 1]}
for something in huu:
    gg = ggey.get(something)
    print(gg)