mem = input("Membership (y/n) : ")
amount = float(input("Total amount : "))
Discount = 0

if mem == 'y':
    if amount >= 1000:
        Discount_per = 20
    elif amount >= 500:
        Discount_per = 10
    else:
        Discount_per = 0
else:
    if amount >= 1000:
        Discount_per = 5
    else:
        Discount_per = 0

Discount = (amount/100)*Discount_per
print("Discount : %.2f" %Discount)
total = amount-Discount
print("Final Amount to Pay : %.2f" %total)