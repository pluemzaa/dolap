member = input("Membership (y/n) : ")
price = int(input("Total amount : "))

if member == "y":
    if price >= 1000:
        Discount = price * (20/100)
        print(f"Discount : {Discount:.2f}")
        print(f"Final Amount to Pay : {price-Discount:.2f}")
    elif price >= 500:
        Discount = price * (10/100)
        print(f"Discount : {Discount:.2f}")
        print(f"Final Amount to Pay : {price-Discount:.2f}")
    else:
        Discount = 0
        print(f"Discount : {Discount:.2f}")
        print(f"Final Amount to Pay : {price-Discount:.2f}")
else:
    if price >= 1000:
        Discount = price * (5/100)
        print(f"Discount : {Discount:.2f}")
        print(f"Final Amount to Pay : {price-Discount:.2f}")
    else:
        Discount = 0
        print(f"Discount : {Discount:.2f}")
        print(f"Final Amount to Pay : {price-Discount:.2f}")