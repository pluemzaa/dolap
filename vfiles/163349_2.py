print("Beverage List:")
print("1. Coffee - $2.5 - Quantity: 10")
print("2. Tea - $1.5 - Quantity: 0")
print("3. Juice - $3.0 - Quantity: 2")

Coffee_price = 2.5
Tea_price = 1.5
Juice_price = 3.0
Coffee_Q = 10
Tea_Q = 0
Juice_Q = 2

x = int(input("Enter the number of the beverage you want to purchase: "))
if x == 1 :

    Coffee_count = int(input("Enter the quantity you want to purchase: "))

    if Coffee_count <= 10 :
        total =  Coffee_count*Coffee_price
        print (f"You purchased {Coffee_count:.0f} Coffee for ${total:.1f}")
        print ("Enjoy your drink!")

    else :
        print ("Sorry, Coffee is out of stock")


elif x == 2 :

    Tea_count = int(input("Enter the quantity you want to purchase: "))

    if Tea_count <= 0 :
        total =  Tea_count*Tea_price
        print (f"You purchased {Tea_count:.0f} Tea for ${total:.1f}")
        print ("Enjoy your drink!")
    else : 
        print ("Sorry, Tea is out of stock")   

elif x == 3 :
    Juice_count = int(input("Enter the quantity you want to purchase: "))
    if Juice_count <= 2:
        total =  Juice_count*Juice_price
        print (f"You purchased {Juice_count:.0f} Juice for ${total:.1f}")
        print ("Enjoy your drink!")
    else :
        print ("Sorry, Juice is out of stock")