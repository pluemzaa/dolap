Cp = 2.5
Cq = 10
Tp = 1.5
Tq = 0
Jp = 3.0
Jq = 2
print("Beverage List: ")
print(f"1. Coffee - $2.5 - Quantity: {Cq}")
print(f"2. Tea - $1.5 - Quantity: {Tq}")
print(f"3. Juice - $3.0 - Quantity: {Jq}")

menu = int(input("Enter the number of the beverage you want to purchase: "))
if menu == 1 :
    q = int(input("Enter the quantity you want to purchase: "))
    if q <= Cq :
        m = q * 2.5
        print(f'You purchased {q} Coffee for ${m}')
        print("Enjoy your drink!")
    else :
        print("Sorry, Coffee is out of stock")
elif menu == 2 :
    q = int(input("Enter the quantity you want to purchase: "))
    if q <= Tq :
        m = q * 1.5
        print(f'You purchased {q} Tea for ${m}')
        print("Enjoy your drink!")
    else :
        print("Sorry, Tea is out of stock")
elif menu == 3 :
    q = int(input("Enter the quantity you want to purchase: "))
    if q <= Jq :
        m = q * 3.0
        print(f'You purchased {q} Juice for ${m}')
        print("Enjoy your drink!")
    else :
        print("Sorry, Juice is out of stock")