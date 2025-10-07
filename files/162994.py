#lab1
item = []
weigh = [] 

for i in range(1,5):
    
    fru = input(f"Enter item {i:}:")
    item.append(fru)
    
    w = input(F"Enter weight {i:}:")
    weigh.append(w)
    
weigh = [float(x) for x in weigh]

for i in range(len(item)) :
    print(f"{item[i]}           {weigh[i]:.2f}")
print("---------------------------")
print(f"total           {sum(weigh):.2f}")