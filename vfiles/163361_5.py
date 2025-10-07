print("Beverage List:")
print("1. Coffee - $2.5 - Quantity: 10")
print("2. Tea - $1.5 - Quantity: 0")
print("3. Juice - $3.0 - Quantity: 2")
ty = int(input("Enter the number of the beverage you want to purchase: "))
qw = int(input("Enter the quantity you want to purchase:"))
if qw >=0:
    if ty ==1:
     price=qw*2.5
     if qw<=0: 
        print(f"You purchased {qw}  Coffee for ${price}")
        print("Enjoy your drink!")
    else :
        print("Sorry, coffee is out of stock")
elif ty==2:
    price=qw*1.5
    if qw<=0:
        print(f"You purchased {qw} Tea for ${price}")
        print("Enjoy your drink!")
    else :
        print("Sorry, Tea is out of stock")
elif ty==3:
    price=qw*3.0
    if qw<=0:
        print(f"You purchased {qw} Juice for ${price}")
        print("Enjoy your drink!")
    else:
        print("Sorry, Jucie is out of stock")