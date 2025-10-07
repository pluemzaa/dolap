coffee_quan = 10
juice_quan = 2
tea_quan = 0

coffee_price = 2.5
tea_price = 1.5
Juice_price = 3.0

bev = 0
quan = 0

print("Beverage List:")
print("1.Coffee - $",coffee_price," - Quantity:",coffee_quan)
print("2.Tea - $",tea_price," - Quantity:",tea_quan)
print("3.Juice - $",Juice_price," - Quantity:",juice_quan)

bev = int(input("Enter the number of the beverage you want to puchase: "))
quan = int(input("Enter the quantity you want to purchase: "))

if bev == 1:
    if coffee_quan >= quan:
        print("You purchased",quan,"coffee for $",coffee_price*quan,"\nEnjoy your drink!")
        coffee_quan -= quan
    else:
      print("Sorry, Coffee is out of stock")
if bev == 2: 
    print("Sorry, Tea is out of stock")
if bev == 3:
    if juice_quan >= quan:
        print("You purchased",quan,"juice for $",Juice_price*quan,"\nEnjoy your drink!")
        juice_quan -= quan
    else:
      print("Sorry, Juice is out of stock")



#if tea_quan >= quan:
#    print("You purchased",quan,"tea for $",tea_price*quan,"\nEnjoy your drink!")
#    tea_quan -= quan
#else: