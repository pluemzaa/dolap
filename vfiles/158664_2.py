cokePrice = 25
print("please select")
print("1 Coke")
print("2 Pepsi")
menu = int(input())
if menu == 1:
    print("You selected Coke")
    print("Price " + str(cokePrice) + "Baht")
else:
    if menu == 2:
        print("You selected Pepsi")
        print("Price 15 Baht")
    else:
        print("invalid menu")