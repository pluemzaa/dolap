t = float(input("Total amount : "))
Member = input("Membership (y/n) : ")
if Member == 'y':
    if t >= 1000:
        Discount = t*(20/100)
    elif t >= 500 and t <= 900:
        Discount = t*(10/100)
else:
    Discount == 0
total = t - Discount
print(f"Total amount : {t}")
print(f"Discount : {Discount}")
print(f"Final Amount to Pay : {total:.2f}")