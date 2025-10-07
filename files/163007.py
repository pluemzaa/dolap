weights = []
items = []
samweight = 0
for i in range(1,5):
    item = input(f"Enter item {i} :")
    weight = float(input(f"Enter weight {i} :"))
    items.append(item)
    weights.append(weight)

    samweight += weight


for j in range(4):
        print(f"{items[j]:<20}{weights[j]:.2f}")

print("---------------------------")
print(f"{'total':<20}{samweight:.2f}")