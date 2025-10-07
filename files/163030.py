fruit = []
weight = []
total = 0
for i in range(1,5) :
    f = input(f"Enter item {i} : ")
    w = float(input(f"Enter weight {i} : "))
    total += w
    fruit.append(f)
    weight.append(w)
for i in range(len(fruit)) :
    print(f"{fruit[i]}\t\t{weight[i] : .2f}")
print("---------------------------")
print(f"total\t\t{total : .2f}")