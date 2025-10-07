e = input("Membership (y/n) :")
w = int(input("Total amount :"))
price = 0
t = 0
if e == 'y' :
    if w >= 1000:
        price = (20/100)*w
        t = w-price
        print("Discount :""%.2f"%price)
        print("Final Amount to Pay :""%.2f"%t)
    elif w >= 500 and w < 1000 :
        price = (10/100)*w
        t = w-price
        print("Discount :""%.2f"%price)
        print("Final Amount to Pay :""%.2f"%t)
    else:
        price = 0
        t = w
        print("Discount :""%.2f"%price)
        print("Final Amount to Pay :""%.2f"%t)
elif e == 'n' :
    if w >= 1000:
        price = (5/100)*w
        t = w-price
        print("Discount :""%.2f"%price)
        print("Final Amount to Pay :""%.2f"%t)
    else:
        t = w
        print("Discount :""%.2f"%price)
        print("Final Amount to Pay :""%.2f"%t)