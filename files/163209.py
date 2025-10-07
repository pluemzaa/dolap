items = []
weight = []

i1 = input("Enter item 1 :")
items.append(i1)
w1 = float(input("Enter weight 1 :"))
weight.append(w1)
i2 = input("Enter item 2 :")
items.append(i2)
w2 = float(input("Enter weight 2 :"))
weight.append(w2)
i3 = input("Enter item 3 :")
items.append(i3)
w3 = float(input("Enter weight 3 :"))
weight.append(w3)
i4 = input("Enter item 4 :")
items.append(i4)
w4 = float(input("Enter weight 4 :"))
weight.append(w4)

print(items[0],"           %.2f" %weight[0])
print(items[1],"           %.2f" %weight[1])
print(items[2],"           %.2f" %weight[2])
print(items[3],"           %.2f" %weight[3])
print("---------------------------")
total = weight[0] + weight[1] + weight[2] + weight[3]
print("total           %.2f" %total)