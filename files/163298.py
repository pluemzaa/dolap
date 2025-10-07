member = str(input("Membership (y/n) : "))
total = float(input("Total amount : "))
if member == 'y':
    if total >= 1000:
        print(f"Discount : {total*0.2:.2f}")
        print(f"Final Amount to Pay : {(total-(total*0.2)):.2f}")
    elif total >= 500:
        if total <= 999:
            print(f"Discount : {total*0.1:.2f}")
            print(f"Final Amount to Pay : {(total-(total*0.1)):.2f}")
    else:
        print("Discount : 0.00")
        print(f"Final Amount to Pay : {total:.2f}")
elif member == 'n':
    if total >= 1000:
        print(f"Discount : {total*0.05:.2f}")
        print(f"Final Amount to Pay : {(total-(total*0.05)):.2f}")
    else:
        print("Discount : 0.00")
        print(f"Final Amount to Pay : {total:.2f}")