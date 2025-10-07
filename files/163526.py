coffee_price=2.5
coffee_qty=10
tea_price = 1.5
tea_qty=0
juice_price=3.0
juice_qty=2
print("""Beverage List:
1. Coffee - $2.5 - Quantity: 10
2. Tea - $1.5 - Quantity: 0
3. Juice - $3.0 - Quantity: 2""")
c= int(input("Enter the number of the beverage you want to purchase:"))
qty = int(input("Enter the quantity you want to purchase:"))
if c==1:
    if coffee_qty<qty:
        print("Sorry, Coffee is out of stock")
    else:
        total = coffee_price*qty
        print(f"You purchased {qty} Coffee for ${total}")
        print("Enjoy your drink!")
elif c==2:
    if tea_qty<qty:
        print("Sorry, Tea is out of stock")
    else:
        total = tea_price*qty
        print(f"You purchased {qty} Tea for ${total}")
        print("Enjoy your drink!")
elif c==3:
    if juice_qty<qty:
        print("Sorry, juice is out of stock")
    else:
        total = juice_price*qty
        print(f"You purchased {qty} Juice for ${total}")
        print("Enjoy your drink!")