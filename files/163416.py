items = []
weights = []

for i in range(1, 5):
    item = input(f"Enter item {i} : ").strip()
    weight = float(input(f"Enter weight {i} : "))
    items.append(item)
    weights.append(weight)

for i in range(4):
    print(f"{items[i]:<15}{weights[i]:>10.2f}")

print("-" * 27)
print(f"{'total':<15}{sum(weights):>10.2f}")