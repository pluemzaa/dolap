m = input("Membership (y/n) : ")
am = float(input("Total amount : "))
d = 0
if m == "y":
    if am >= 1000:
        d = am*(20/100)
    elif am >=500 and am <= 999:
        d = am*(10/100)
    else:
        d = 0
if m == "n":
    if am >= 1000:
        d = am*(5/100)
    else:
        d = 0
fam = am - d
print("Discount : %.2f"%d)
print("Final Amount to Pay : %.2f"%fam)