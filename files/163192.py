cost = 0

item = []

fruit1 = str(input("Enter item 1 : "))
weigth1 = float(input("Enter weight 1 : "))

fruit2 = str(input("Enter item 2 : "))
weigth2 = float(input("Enter weight 2 : "))

fruit3 = str(input("Enter item 3 : "))
weigth3 = float(input("Enter weight 3 : "))

fruit4 = str(input("Enter item 4 : "))
weigth4 = float(input("Enter weight 4 : "))

total = weigth1 + weigth2 + weigth3 + weigth4 
item.append([fruit1,weigth1])
item.append([fruit2,weigth2])
item.append([fruit3,weigth3])
item.append([fruit4,weigth4])

for i in range(len(item)):
    print(f"{item[i][0]}                   {item[i][1]:.2f}")

print("---------------------------")
print(f"Total                     {total:.2f}")