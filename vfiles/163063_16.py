mem = input("Membership (y/n) : ")
amount = float(input("Total amount : "))

if mem == 'y':
    if amount >= 1000:
        rate = 0.20
    elif amount >= 500:
        rate = 0.10
    else:
        rate = 0.00
else:
    if amount >= 1000:
        rate = 0.05
    else:
        rate = 0.00

discount = amount * rate
final_amount = amount - discount

print()
print(f"Discount : {discount:.2f}")
print(f"Final Amount to Pay : {final_amount:.2f}")