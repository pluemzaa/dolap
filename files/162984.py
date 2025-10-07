list_item = []
list_weight = []
for i in range(1,5):
    item = input(f"Enter item {i} : ")
    weight = float(input(f"Enter weight {i} : "))
    list_item.append(item)
    list_weight.append(weight)
for i in range (0,4):
    print (f"{list_item[i]}\t\t{list_weight[i]:.2f}")
print("---------------------------")
print (f"total\t\t{sum(list_weight):.2f}")