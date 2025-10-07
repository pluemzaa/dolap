cQty = 10
tQty = 0
totalPrice = 0
print("Beverage List:")
print("1. Coffee - 25 Baht - Qty: 10")
print("2. Tea - 20 Baht - Qty: 0")
print("Select menu (1 = Coffee, 2 = Tea): ")
reqMenu = int(input())
print("Enter quantity:")
reqQty = int(input())
if reqMenu == 1:
    if reqQty <= cQty and reqQty > 0:
        totalPrice = 25 * reqQty
        print("You purchased Coffee")
        print("Total Price : " + str(totalPrice) + " Baht")
        print("Enjoy!")
    else:
        print("Sorry, Coffee out of stock")
else:
    if reqQty <= tQty and reqQty > 0:
        totalPrice = 20 * reqQty
        print("You purchased Tea")
        print("Total Price : " + str(totalPrice) + " Baht")
        print("Enjoy!")
    else:
        print("Sorry, Tea out of stock")