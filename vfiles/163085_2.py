m = (input("Membership (y/n) : "))
if m == "y":
    t = int(input("Total amount : "))
    if t >= 1000:
           d = (t * 20) / 100
           print("Discount : %.2f" % (d))
           f = t - d
           print("Final Amount to Pay : %.2f" % (f))
    elif 500 <= t < 1000:
        d = (t * 10) / 100
        print("Discount : %.2f" % (d))
        f = t - d
        print("Final Amount to Pay : %.2f" % (f))
    elif t < 1000:
        d = 0
        print("Discount : %.2f" % (d))
        f = t - d
        print("Final Amount to Pay : %.2f" % (f))
if m == "n":
    t = int(input("Total amount : "))
    if t >= 1000:
           d = (t * 5) / 100
           print("Discount : %.2f" % (d))
           f = t - d
           print("Final Amount to Pay : %.2f" % (f))
    elif t < 1000:
        d = 0
        print("Discount : %.2f" % (d))
        f = t - d
        print("Final Amount to Pay : %.2f" % (f))