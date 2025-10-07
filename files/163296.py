me = str(input("Membership (y/n) : "))
totol = float(input("Total amount : "))
if me == 'y':
    if totol >= 1000:
        print(f"Discount : {totol*0.2:.2f}")
        print(f"Final Amount to Pay : {totol - (totol*0.2):.2f}")
    elif totol >= 500:
        if totol <= 999:
            print(f"Discount : {totol*0.1:.2f}")
            print(f"Final Amount to Pay : {totol-(totol*0.1):.2f}")
    else:
        print("Discount : 0.00")
        print(f"Final Amount to Pay : {totol:.2f}")

elif me == 'n':
    if totol >= 1000:
        print(f"Discount : {totol*0.05:.2f}")
        print(f"Final Amount to Pay : {totol - (totol*0.05):.2f}")
    else:
        print("Discount : 0.00")
        print(f"Final Amount to Pay : {totol:.2f}")