n = 4
items = []
w = []

for i in range(n):
    print("Enter item", i + 1,end=' ')
    item = input(":")
    items.append(item)
    
    print("Enter weight", i + 1, end=' ')
    weight = float(input(":"))
    w.append(weight)
    
total = 0
for i in range(len(items)):
    total += w[i]
    print(items[i],f"{w[i]:.2f}")
print("---------------------------  ")
print(f"total {total:.2f}")