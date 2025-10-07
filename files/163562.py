member = input("Membership (y/n) : ")

amount = float(input("Total amount : "))


if member == "y":
    if amount >= 1000:
        discount = amount * 0.20
    elif amount >= 500:
        discount = amount * 0.10
    else:
        discount = 0.0
else:
    if amount >= 1000:
        discount = amount * 0.05
    else:
        discount = 0.0

final_amount = amount - discount


print(f"\nDiscount : {discount:.2f}")
print(f"Final Amount to Pay : {final_amount:.2f}")