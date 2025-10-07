M = (input("Membership (y/n) : "))
t = float(input("Total amount : "))
discount = 0
if M == 'y':
    if t >= 1000:
        discount = t * 0.2
    elif t >=500:
        discount = t * 0.1
else:
    if t >=1000:
        discount = t * 0.05
ta = t - discount
print(f"Discount : {discount:.2f}")
print(f"Final Amount to Pay : {ta:.2f}")