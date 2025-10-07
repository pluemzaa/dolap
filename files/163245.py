a = input("Membership (y/n) : ")
b = float(input("Total amount : "))

if a == "y":
    if b >= 1000:
        c = b*0.2
        print(f"Discount : {c:.2f}")
        print(f"Final Amount to Pay : {b - c:.2f}")
    elif b >= 500 and b <= 999:
        c = b*0.1
        print(f"Discount : {c:.2f}")
        print(f"Final Amount to Pay : {b - c:.2f}")
    else:
        c = b*0
        print(f"Discount : {c:.2f}")
        print(f"Final Amount to Pay : {b - c:.2f}")
elif a == "n":
    if b >= 1000:
        c = b*0.05
        print(f"Discount : {c:.2f}")
        print(f"Final Amount to Pay : {b - c:.2f}")
    else:
        c = b*0
        print(f"Discount : {c:.2f}")
        print(f"Final Amount to Pay : {b - c:.2f}")