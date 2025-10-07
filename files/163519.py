mem = input("Membership (y/n) : ")
total = int(input("Total amount : "))

if mem == "y":
    if total >= 1000:
        discount = (total*20)/100
        print(f"Discount : {discount:.2f}")
        total -= discount
        print(f"Final Amount to Pay : {total:.2f}")
        
    elif total >= 500 and total < 1000:
        discount = (total*10)/100
        print(f"Discount : {discount:.2f}")
        total -= discount
        print(f"Final Amount to Pay : {total:.2f}")
    else:
        discount = 0
        print(f"Discount : {discount:.2f}")
        print(f"Final Amount to Pay : {total:.2f}")

if mem != "y":
    if total >= 1000:
        discount = (total*5)/100
        print(f"Discount : {discount:.2f}")
        total -= discount
        print(f"Final Amount to Pay : {total:.2f}")
        
    else:
        discount = 0
        print(f"Discount : {discount:.2f}")
        print(f"Final Amount to Pay : {total:.2f}")