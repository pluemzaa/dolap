m = str(input("Membership (y/n) : "))
a = float(input("Total amount : "))
if m == "y" :
    if 500<=a<=999:
        d = a*0.1
        print(f"Discount : {d:.2f}")
        f = a - d
        print(f"Final Amount to Pay : {f:.2f}")
    elif a>=1000:
        d = a*0.2
        print(f"Discount : {d:.2f}")
        f = a - d
        print(f"Final Amount to Pay : {f:.2f}")
    else:
        d = 0
        print(f"Discount : {d:.2f}")
        f = a - d
        print(f"Final Amount to Pay : {f:.2f}")
else:
    if a>=1000:
        d = a*0.05
        print(f"Discount : {d:.2f}")
        f = a - d
        print(f"Final Amount to Pay : {f:.2f}")
    else:
        d = 0
        print(f"Discount : {d:.2f}")
        f = a - d
        print(f"Final Amount to Pay : {f:.2f}")