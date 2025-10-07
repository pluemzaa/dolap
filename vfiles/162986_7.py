l1 = []
l2 = []
for i in range(1,5):
    x = input(f"Enter item {i} : ")
    y = float(input(f"Enter weight {i} : "))
    l1.append(x)
    l2.append(y)
sum = sum(l2)
for i in range(len(l1)):
    print(f"{l1[i]}           {l2[i]:.2f}")
print('---------------------------')
print(f"total                     {sum:.2f}")