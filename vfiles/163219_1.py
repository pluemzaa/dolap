item1 = input("Enter item 1 : ")
w1 = float(input("Enter weight 1 : "))
item2 = input("Enter item 2 : ")
w2 = float(input("Enter weight 2 : "))
item3 = input("Enter item 3 : ")
w3 = float(input("Enter weight 3 : "))
item4 = input("Enter item 4 : ")
w4 = float(input("Enter weight 4 : "))

total = w1+w2+w3+w4

print(f"{item1}           {w1:.2f}")
print(f"{item2}           {w2:.2f}")
print(f"{item3}           {w3:.2f}")
print(f"{item4}           {w4:.2f}")
print("---------------------------")

print("%.2f" % total)