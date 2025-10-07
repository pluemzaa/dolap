membership = input("Membership (y/n) : ").lower()
total = float(input("Total amount : "))

if membership == 'y':
    if total >= 1000:
        discount = total * 0.20
    elif total >= 500:
        discount = total * 0.10
    else:
        discount = 0.0
else:
    if total >= 1000:
        discount = total * 0.05
    else:
        discount = 0.0

final_amount = total - discount

print(f"Discount : {discount:.2f}")
print(f"Final Amount to Pay : {final_amount:.2f}")