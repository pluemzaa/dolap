membership = input("Membership (y/n) :")

if membership == "y" :
    total = int(input("Total amount : "))
    if total > 999 :
        discount = total * (1/5)
    elif total > 499 :
        discount = total * (1/10)
    else :
        discount = 0
    print ("Discount : %.2f" %discount)

    final = total - discount
    print ("Final Amount to Pay : %.2f" %final)
else :
    total = int(input("Total amount : "))
    if total > 999 :
        discount = total * (1/20)
    else :
        discount = 0
    print ("Discount : %.2f" %discount)

    final = total - discount
    print ("Final Amount to Pay : %.2f" %final)