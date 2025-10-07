items = []
weights = []

for i in range(1, 5):
    item = input(f"Enter item {i} :").strip()
    weight = float(input(f"Enter weight {i} :"))
    items.append(item)
    weights.append(weight)

for i in range(4):
    print(f"{items[i]:<20}{weights[i]:>7.2f}")

print('-' * 27)
total_weight = sum(weights)
print(f"{'Total':<20}{total_weight:>7.2f}")