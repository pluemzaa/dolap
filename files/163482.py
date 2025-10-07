items = []
weights = []
total = 0

for i in range(1,5):
    item = input(f"Enter item {i} :")
    weight = float(input((f"Enter weight {i} :")))
    items.append(item)
    weights.append(weight)
    total += weight

for i in range(4):
    print(f"{items[i]:<20}{weights[i]:>10.2f}")

print("-"*27)
print(f"{'total':<20}{total:>10.2f}")