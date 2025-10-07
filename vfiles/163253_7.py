F1 = input("Enter item 1 : ")
FW1 = float(input("Enter weight 1 : "))
F2 = input("Enter item 2 : ")
FW2 = float(input("Enter weight 2 : "))
F3 = input("Enter item 3 : ")
FW3 = float(input("Enter weight 3 : "))
F4 = input("Enter item 4 : ")
FW4 = float(input("Enter weight 4 : "))

total = FW1 + FW2 + FW3 + FW4

print(f"{F1:<20}{FW1:>7.2f}")
print(f"{F2:<20}{FW2:>7.2f}")
print(f"{F3:<20}{FW3:>7.2f}")
print(f"{F4:<20}{FW4:>7.2f}")
print("---------------------------")
print(f"{'total':<20}{total:>7.2f}")