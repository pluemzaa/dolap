items = []
weights = []

for i in range(1,5,1):
    name = str(input(f"Enter item {i} :"))
    items.append(name)

    weight = float(input(f"Enter weight {i} :"))
    weights.append(weight)

#print()  # ขึ้นบรรทัดใหม่

for i in range(len(items)):
    print(items[i],end = ""),print("           ",end=""),print(f"{weights[i]:.2f}")


print('---------------------------')
total = sum(weights)
total = float(total)
print(f"Total           {total:.2f}")