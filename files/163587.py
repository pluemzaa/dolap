print("Beverage List:")
print("1. Coffee - $2.5 - Quantity:")
print("2. Tea - $1.5 - Quantity: 0")
print("3. Juice - $3.0 - Quantity: 2")

coffee_price=2.5
Tea_price=1.5
Juice_price=3.0


num = int(input("Enter the number of the beverage you want to purchase: "))
if num==1:

    c_cou = int(input("Enter the quantity you want to purchase:"))

    if c_cou <=10:
        total= coffee_price*c_cou
        print (f"You purchased{c_cou:.2f}Coffee for{total:.2f}")
        print ("Enjoy your drink!")

    else:
        print ("Sorry, Coffee is out of stock")


elif num==2:

    t_cou = int(input("Enter the quantity you want to purchase: "))

    if t_cou <=0:
        total= Tea_price*t_cou
        print (f"You purchased{c_cou:.2f}Coffee for{total:.2f}")
        print ("Enjoy your drink!")

    else:
        print("Sorry, Tea is out of stock")    
        
elif num == 3 :

    j_cou = int(input("Enter the quantity you want to purchase: "))
    
    if  j_cou <= 2:
        total =  j_cou*Juice_price
        print (f"You purchased {j_cou:.0f} Juice for ${total:.1f}")
        print ("Enjoy your drink!")
    else :
        print ("Sorry, Juice is out of stock")