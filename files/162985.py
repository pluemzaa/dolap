a = []
t = 0

for i in range(4):
   it = input(f"Enter item {i + 1} : ")
   w = input(f"Enter weight {i + 1} : ")
   
   a.append([it,float(w)])
   
for j in range(len(a)):
    l = a[j]
    
    print(f"{l[0]} \t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t {l[1]:.2f}")
    
    t += l[1]

print("---------------------------")
print(f"total \t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t {t:.2f}")