membership = input("Membership (y/n) : ")
amount = float(input("Total amount : "))

discount = 0.0

if membership == 'y' or membership == 'Y':
    if amount >= 1000:
        discount = amount * 0.20
    elif amount >= 500:
        discount = amount * 0.10
elif membership == 'n' or membership == 'N':
    if amount >= 1000:
        discount = amount * 0.05

final_amount = amount - discount

print(f"Discount : {discount:.2f}")
print(f"Final Amount to Pay : {final_amount:.2f}")