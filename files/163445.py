total = 0
items = []

for i in range(1, 5):
    name = input(f"Enter item {i} : ")
    weight = float(input(f"Enter weight {i} : "))
    items.append((name, weight))
    total += weight

for item, weight in items:
    print(f"{item:<15}{weight:>7.2f}")

print("---------------------------")
print(f"{'total':<15}{total:>7.2f}")