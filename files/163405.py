items = []
weights = []
total = 0

# รับข้อมูล 4 ชุด
for i in range(1, 5):
    item = input(f"Enter item {i} : ").strip()
    weight = float(input(f"Enter weight {i} : "))
    items.append(item)
    weights.append(weight)
    total += weight

# แสดงข้อมูล
for i in range(4):
    print(f"{items[i]:<15}{weights[i]:>10.2f}")

print("-" * 27)
print(f"{'total':<15}{total:>10.2f}")