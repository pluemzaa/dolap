item = []
p = []
for i in range (4):
    item.append(input(f"Enter item {i+1} :"))
    p.append(float(input(f"Enter weight {i+1} :")))

sum = sum(p)   
for i in range(4):
    print(f"{item[i]}                    {p[i]:.2f}")
print("---------------------------")
print(f"total                     {sum:.2f}")