items = []
weights = []

for i in range(1,5):
    item = input(f"Enter item{i} : ")
    weight = float(input(f"Enter weight {i} : "))
    items.append(item)
    weights.append(weight)

for i in range(4):
    print(f"{item[i]:<15}{weights[i]:.2f}")

print("---------------------------")

Total_weight = sum(weights)
print(f"{'Total':<15}{Total_weight:.2f}")