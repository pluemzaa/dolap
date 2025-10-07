member = input("Membership (y/n) : ")
total_a = float(input("Total amount : "))
Discount = 0
final = 0
if member == 'y' :
    if total_a >= 1000 :
        Discount = total_a * 0.2
        final = total_a - Discount
        print(f"Discount : {Discount:.2f} ")
        print(f"Final Amount to Pay : {final:.2f}" )
    elif total_a >=500 and total_a <=999 :
        Discount = total_a * 0.1
        final = total_a - Discount
        print(f"Discount : {Discount:.2f} ")
        print(f"Final Amount to Pay : {final:.2f}" )
    elif total_a < 500 :
        Discount = total_a * 0
        final = total_a - Discount
        print(f"Discount : {Discount:.2f} ")
        print(f"Final Amount to Pay : {final:.2f}" )
elif member == 'n' :
    if total_a >= 1000 :
        Discount = total_a * 0.05
        final = total_a - Discount
        print(f"Discount : {Discount:.2f} ")
        print(f"Final Amount to Pay : {final:.2f}" )
    elif total_a < 1000 :
        Discount = total_a * 0
        final = total_a - Discount
        print(f"Discount : {Discount:.2f} ")
        print(f"Final Amount to Pay : {final:.2f}" )