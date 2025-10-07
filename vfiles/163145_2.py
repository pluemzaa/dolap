M_ship = input("Membership (y/n) : ")
Buy = int(input('Total amount : '))

if M_ship == "y" and Buy >= 1000:
    discount = (Buy * 20) / 100
    final = Buy - discount
    print("Membership (y/n) : y")
    print(f"Total amount : {Buy}")
    print(f"Discount : {discount}")
    print(f"Final Amount to Pay : {final}")
    
elif M_ship == "y" and Buy >= 500 and Buy <= 999:
    discount = (Buy * 10) / 100
    final = Buy - discount
    print("Membership (y/n) : y")
    print(f"Total amount : {Buy}")
    print(f"Discount : {discount}")
    print(f"Final Amount to Pay : {final}")
    
elif M_ship != "n" and Buy >= 1000:
    discount = (Buy * 5) / 100
    final = Buy - discount
    print("Membership (y/n) : y")
    print(f"Total amount : {Buy}")
    print(f"Discount : {discount}")
    print(f"Final Amount to Pay : {final}")
    
else:
    print(f"Membership (y/n) : {M_ship}")
    print(f"Total amount : {Buy}")
    print(f"Discount : 0.00")
    print(f"Final Amount to Pay : {Buy}")