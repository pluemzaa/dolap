Fruit = input("Enter item 1 : ")
Weight = float(input("Enter weight 1 : "))
Fruit_2 = input("Enter item 2 : ")
Weight_2 = float(input("Enter weight 2 : "))
Fruit_3 = input("Enter item 3 : ")
Weight_3 = float(input("Enter weight 3 : "))
Fruit_4 = input("Enter item 4 : ")
Weight_4 = float(input("Enter weight 4 : "))

total = Weight + Weight_2 + Weight_3 + Weight_4


print(f"{Fruit}           {Weight:.2f}")
print(f"{Fruit_2}          {Weight_2:.2f}")
print(f"{Fruit_3}          {Weight_3:.2f}")
print(f"{Fruit_4}          {Weight_4:.2f}")
print(f"---------------------------")
print(f"total           {total:.2f}")