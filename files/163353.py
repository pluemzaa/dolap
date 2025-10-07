print("Beverage List:")
print("1. Coffee - $2.5 - Quantity: 10")
print("2. Tea - $1.5 - Quantity: 0")
print("3. Juice - $3.0 - Quantity: 2")
type=int(input("Enter the number of the beverage you want to purchase: "))
quan=int(input("Enter the quantity you want to purchase: "))
if quan>=0:
    if type==1:
        if quan<=10:
            tol=2.5*quan
            print(f"You purchased {quan} Coffee for ${tol}")
            print("Enjoy your drink!")
        else:
            print("Sorry, Coffee is out of stock")
    elif type==2:
        if quan<=0:
            tol=1.5*quan
            print(f"You purchased {quan} Tea for ${tol}")
            print("Enjoy your drink!")
        else:
            print("Sorry, Tea is out of stock")
    elif type==3:
        if quan<=2:
            tol=3.0*quan
            print(f"You purchased {quan} Juice for ${tol}")
            print("Enjoy your drink!")
        else:
            print("Sorry, Juice is out of stock")
else:
    pass