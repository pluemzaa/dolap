print("Beverage List:")
c = 2.5
cq = 10
print("1. Coffee - $2.5 - Quantity: 10")
print("2. Tea - $1.5 - Quantity: 0")
j = 3.0
jq = 2
print("3. Juice - $3.0 - Quantity: 2")

bev = int(input("Enter the number of the beverage you want to purchase:"))
qua = int(input("Enter the quantity you want to purchase: "))

if bev == 1:
    total = qua * c
    print("You purchased",qua,f"Coffee for ${total}")
    print("Enjoy your drink!")
elif bev == 2:
    print("Sorry, Tea is out of stock")
elif bev == 3:
    if qua >2 :
        print("Sorry, juice is out of stock")
    else:
        total = qua * j
        print("You purchased",qua,f"Juice for ${total}")
        print("Enjoy your drink!")