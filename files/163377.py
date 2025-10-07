items = []
weights = []

for i in range(4):
    item = input(f"Enter item {i + 1} :")
    weight = float(input(f"Enter weight {i + 1} :"))
    items.append(item)
    weights.append(weight)

total_weight = sum(weights)

for i in range(4):
    print(f"{items[i]:<20}{weights[i]:>7.2f}")

print("---------------------------")
print(f"{'Total':<20}{total_weight:>7.2f}")