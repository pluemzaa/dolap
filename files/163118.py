member =input("Membership (y/n) : ")
total = float(input("Total amount : "))
if member == "y":
    if total >= 1000:
        discount = total * 0.2
        print("Discount : %.2f" % discount)
        print("Final Amount to Pay : %.2f" % (total - discount))
    elif 500 <= total < 999:
        discount = total * 0.1
        print("Discount : %.2f" % discount)
        print("Final Amount to Pay : %.2f" % (total - discount))
    else:
        discount = 0
        print("Discount : %.2f" % discount)
        print("Final Amount to Pay : %.2f" % total)
elif member == "n":
    if total >= 1000:
        discount = total * 0.05
        print("Discount : %.2f" % discount)
        print("Final Amount to Pay : %.2f" % (total - discount))
    else:
        discount = 0
        print("Discount : %.2f" % discount)
        print("Final Amount to Pay : %.2f" % total)