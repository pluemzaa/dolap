coffee=10
pri_coffee=2.5
tea=0
pri_tea=1.5
juice=2
pri_juice=3.0
print("Beverage List:")
print("1. Coffee - $2.5 - Quantity: 10")
print("2. Tea - $1.5 - Quantity: 0")
print("3. Juice - $3.0 - Quantity: 2")
b=input("Enter the number of the beverage you want to purchase: ")
c=int(input("Enter the quantity you want to purchase: "))
if b =="1":
    if c<=coffee:
        total= pri_coffee*c
        print(f"You purchased {c} Coffee for ${total}")
        print("Enjoy your drink!")
    else:
        print("Sorry, Coffee is out of stock")
elif b =="2":
        if c<=tea:
            total= pri_tea*c
            print(f"You purchased {c} Tea for ${total}")
            print("Enjoy your drink!")
        else:
            print("Sorry, Tea is out of stock")
elif b =="3":
    if c<juice:
        total= pri_juice*c
        print(f"You purchased {c} Juice for ${total}")
        print("Enjoy your drink!")
      else:
        print("Sorry, Juice is out of stock")