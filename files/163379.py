a = input("Enter item 1 : ")
a1 = input("Enter weight 1 : ")
p = input("Enter item 2 : ")
p1 = input("Enter weight 2 : ")
b = input("Enter item 3 : ")
b1 = input("Enter weight 3 : ")
o = input("Enter item 4 : ")
o1 = input("Enter weight 4 : ")

a1 = float(a1)
p1 = float(p1)
b1 = float(b1)
o1 = float(o1)

total = a1 + p1 + b1 + o1

print(f"{a}           {a1:.2f} ")
print(f"{p}           {p1:.2f} ") 
print(f"{b}           {b1:.2f} ") 
print(f"{o}           {o1:.2f} ")
print("---------------------------  ")
print(f"total           {total:.2f}")