item1 = input("Enter item 1 : ")
weight1 = float(input("Enter weight 1 : "))
item2 = input("Enter item 2 : ")
weight2 = float(input("Enter weight 2 : "))

item3 = input("Enter item 3 : ")
weight3 = float(input("Enter weight 3 : "))

item4 = input("Enter item 4 : ")
weight4 = float(input("Enter weight 4 : "))


total_weight = weight1 + weight2 + weight3 + weight4

print(f"{item1:<15}{weight1:.2f}")
print(f"{item2:<15}{weight2:.2f}")
print(f"{item3:<15}{weight3:.2f}")
print(f"{item4:<15}{weight4:.2f}")
print("---------------------------")
print(f"{'total':<15}{total_weight:.2f}")