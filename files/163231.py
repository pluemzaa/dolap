lt = []
we = []

for i in range(4) :
    lt.append(input(f"Enter item {i+1} : "))
    we.append(float(input(f"Enter weight {i+1} : ")))
x = 0
for j in range(4):
    print(f"{lt[j]}           {we[j]:.2f}")
    x += we[j]
    
print("---------------------------")
print(f"total            {x:.2f}")