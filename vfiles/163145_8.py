M_ship = input("Membership (y/n) : ")
Buy = float(input('Total amount : '))

if M_ship == "y" and Buy >= 1000:
    discount = (Buy * 20) / 100
    final = Buy - discount
    print(f"Discount : {discount:.2f}")
    print(f"Final Amount to Pay : {final:.2f}")
    
elif M_ship == "y" and Buy >= 500 and Buy <= 999:
    discount = (Buy * 10) / 100
    final = Buy - discount
    print(f"Discount : {discount:.2f}")
    print(f"Final Amount to Pay : {final:.2f}")
    
elif M_ship != "n" and Buy >= 1000:
    discount = (Buy * 5) / 100
    final = Buy - discount
    print(f"Discount : {discount:.2f}")
    print(f"Final Amount to Pay : {final:.2f}")
    
else:
    discount = 0.00
    print(f"Discount : {discount:.2f}")
    print(f"Final Amount to Pay : {Buy:.2f}")