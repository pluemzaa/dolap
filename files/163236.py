print("Beverage List:\n1. Coffee - $2.5 - Quantity: 10\n2. Tea - $1.5 - Quantity: 0\n3. Juice - $3.0 - Quantity: 2")
b = input("Enter the number of the beverage you want to purchase: ")
q = int(input("Enter the quantity you want to purchase: "))
qc = 10
qt = 0
qj = 2
cc = 2.5
ct = 1.5
cj = 3.0
if b == "1":
    if q <= qc:
        print(f"You purchased {q} Coffee for ${cc * q}")
        print("Enjoy your drink!")
    else:
        print("Sorry, Coffee is out of stock")
elif b == "2":
    if q <= qt:
        print(f"You purchased {q} Tea for ${ct * q}")
        print("Enjoy your drink!")
    else:
        print("Sorry, Tea is out of stock")
elif b == "3":
    if q <= qj:
        print(f"You purchased {q} Juice for ${cj * q}")
        print("Enjoy your drink!")  
    else:
        print("Sorry, Juice is out of stock")