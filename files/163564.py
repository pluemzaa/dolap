mb = str(input("Membership (y/n): "))
ta = float(input("Total amount: "))

fa = 0

if ta < 500:
    print("Discount : 0.00")
    print("Final Amount to Pay : %.2f" % ta)

elif mb == "y" and ta >= 1000:
    ds = (ta * 20) / 100
    fa = ta - ds
    print("Discount : %.2f" % ds)
    print("Final Amount to Pay : %.2f" % fa)

elif mb == "y" and ta >= 500:
    ds = (ta * 10) / 100
    fa = ta - ds
    print("Discount : %.2f" % ds)
    print("Final Amount to Pay : %.2f" % fa)

elif mb == "n" and ta >= 1000:
    ds = (ta * 5) / 100
    fa = ta - ds
    print("Discount : %.2f" % ds)
    print("Final Amount to Pay : %.2f" % fa)

else:
    print("Discount : 0.00")
    print("Final Amount to Pay : %.2f" % ta)