items = []
weights = []
total = 0.0

for i in range(1, 5):
    item = input(f"Enter item {i} : ")
    weight = float(input(f"Enter weight {i} : "))
    items.append(item)
    weights.append(weight)
    total += weight

for i in range(4):
    print(f"{items[i]:<15}{weights[i]:>7.2f}")

print("---------------------------")
print(f"{'total':<15}{total:>7.2f}")