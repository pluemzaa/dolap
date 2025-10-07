mem = input("Membership (y/n) :")
amo = int(input("Total amount :"))
if mem == "y":
    if amo >= 1000:
        dis = float(amo*20/100)
        total = amo - dis
    elif amo >= 500:
        dis =float(amo*10/100)
        total = amo - dis
    else:
        dis = 0
        total = amo
else:
    if amo >= 1000:
        dis = float(amo*5/100)
        total = amo - dis
    else:
        dis = 0
        total = amo
print(f"Discount : {dis:.2f}")
print(f"Final Amount to Pay : {total:.2f}")