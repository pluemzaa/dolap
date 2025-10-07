item1=str(input("Enter item 1 :"))
weight1=float(input("Enter weight 1 :"))
item2=str(input("Enter item 2 :"))
weight2=float(input("Enter weight 2 :"))
item3=str(input("Enter item 3 :"))
weight3=float(input("Enter weight 3 :"))
item4=str(input("Enter item 4 :"))
weight4=float(input("Enter weight 4 :"))

print(f"{item1}\t{weight1:.2f}")
print(f"{item2}\t{weight2:.2f}")
print(f"{item3}\t{weight3:.2f}")
print(f"{item4}\t{weight4:.2f}")
print("---------------------------")
total = weight1 + weight2 + weight3 + weight4

print(f"Total\t{total:.2f}")