member = input("Membership (y/n) : ")
amount = float(input("Total amount : "))

discount = 0

if member == 'y':
    if amount >= 1000:
        discount = amount * 0.20
    elif amount >= 500:
        discount = amount * 0.10
elif member == 'n':
    if amount >= 1000:
        discount = amount * 0.05

final = amount - discount

print(f"Discount : {discount:.2f}")
print(f"Final Amount to Pay : {final:.2f}")