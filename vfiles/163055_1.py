total = 0
member = input("Membership (y/n) : ")
total = int(input("Total amount : "))
if member == "y":
    if total >= 1000 :
        discount = 0.2
    elif total < 1000 and total > 500 :
        discount = 0.1
    else :
        discount = 0
else :
    if total >= 1000 :
        discount = 0.05
    else :
            discount = 0
print (f"Discount : {total*discount:.2f}")
print (f"Final Amount to Pay : {(total - (total*discount)):.2f}")