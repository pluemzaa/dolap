mem = input("Membership (y/n) : ")
ta = float(input("Total amount : "))

if mem == "y" :
    if ta >= 1000 :
        dis = ta * 0.20
        print(f"Discount : {dis : .2f}")
        print(f"Final Amount to Pay : {ta - dis : .2f}")
    elif 500 <= ta <= 999 :
        dis = ta * 0.10
        print(f"Discount : {dis : .2f}")
        print(f"Final Amount to Pay : {ta - dis : .2f}")

    else :
        dis = ta * 0.00
        print(f"Discount : {dis : .2f}")
        print(f"Final Amount to Pay : {ta - dis : .2f}")
elif mem == "n" :
    if ta >= 1000 :
        dis = ta * 0.05
        print(f"Discount : {dis : .2f}")
        print(f"Final Amount to Pay : {ta - dis : .2f}")
    else :
        dis = ta * 0.00
        print(f"Discount : {dis : .2f}")
        print(f"Final Amount to Pay : {ta - dis : .2f}")        
else :
    pass