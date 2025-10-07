item = []

for i in range(4):
    it=input(f"Enter item {i+1} :")
    w=float(input(f"Enter weight {i+1} :"))
    item.append([it,w])
    
total = 0
for i in item:
    print(f"{i[0]}        {i[1]:.2f}")
    total += i[1] 
    
print("---------------------------")
print(f"total       {total:.2f}")