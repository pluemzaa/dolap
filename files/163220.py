name = []
valu = []
total = 0
# for i in range(4):
#     n = input("Enter item ")
#     name.append(n)
# print(name)
n = input("Enter item 1 : ")
name.append(n)
v = float(input("Enter weight 1 : "))
valu.append(v)
n = input("Enter item 2 : ")
name.append(n)
v = float(input("Enter weight 2 : "))
valu.append(v)
n = input("Enter item 3 : ")
name.append(n)
v = float(input("Enter weight 3 : "))
valu.append(v)
n = input("Enter item 4 : ")
name.append(n)
v = float(input("Enter weight 4 : "))
valu.append(v)

for i in range(4):
    print(name[i],f"           {valu[i]:.2f}")
    total = total + valu[i]
print("--------------------------- ")
print(f"total           {total:.2f}")