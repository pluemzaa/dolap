items = []
weights = []
total_weight = 0

for i in range(1, 5):
    item = input(f"Enter item {i} : ").strip()
    weight = float(input(f"Enter weight {i} : "))
    items.append(item)
    weights.append(weight)
    total_weight += weight

for i in range(4):
    print(f"{items[i]:<20}{weights[i]:>7.2f}")

print("-" * 27)
print(f"{'total':<20}{total_weight:>7.2f}")