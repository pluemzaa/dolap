a = input("Membership (y/n) : ")
b = float(input("Total amount : "))
c = 0
if a == "y" or a == "n":
    if a == "y":
        if b >= 1000:
            c = b*0.2
            b = b - c
            print(f"Discount : {c:.2f}")
            print(f"Final Amount to Pay : {b:.2f}")
        elif b >= 500:
            c = b*0.1
            b = b - c
            print(f"Discount : {c:.2f}")
            print(f"Final Amount to Pay : {b:.2f}")
        else:
            b = b
            print(f"Discount : {c:.2f}")
            print(f"Final Amount to Pay : {b:.2f}")
    else:
        if b >= 1000:
            c = b*0.05
            b = b - c
            print(f"Discount : {c:.2f}")
            print(f"Final Amount to Pay : {b:.2f}")
        else:
            print("Discount : 0.00")
            print(f"Final Amount to Pay : {b:.2f}")
else:
    print("Discount : 00.00")
    print(f"Final Amount to Pay : {b:.2f}")