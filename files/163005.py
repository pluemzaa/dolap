fruit = []
weight = []

for i in range(0,4,1):
      A = input(f"Enter item {i+1} : ")
      B = float(input(f"Enter weight {i+1} : "))
      fruit.append(A)
      weight.append(B)
      
for i in range(len(fruit)):
      print(f"{fruit[i]}", end=f"\t\t{weight[i]:.2f}\n")
      
print("--------------------------- ")
print(f"total\t\t{sum(weight):.2f}")