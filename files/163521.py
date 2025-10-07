a = input("Membership (y/n) : ")
amount = int(input("Total amount : "))
if a == "y":
    if amount < 500:
        total = 0
        
        print(f"Discount : {total:.2f}")
        print(f"Final Amount to Pay : {amount:.2f}")
    elif amount < 999  :
        total = (10/100) * amount 
        total1 = amount - total
        print(f"Discount : {total:.2f}")
        print(f"Final Amount to Pay : {total1:.2f}")
    elif amount >= 1000:
        total = (20/100) * amount 
        total1 = amount - total
        print(f"Discount : {total:.2f}")
        print(f"Final Amount to Pay : {total1:.2f}")
elif a == "n":
    if amount < 1000:
        total = 0
        
        print(f"Discount : {total:.2f}")
        print(f"Final Amount to Pay : {amount:.2f}")
    elif amount >= 1000:
        total = (5/100) * amount 
        total1 = amount - total
        print(f"Discount : {total:.2f}")
        print(f"Final Amount to Pay : {total1:.2f}")