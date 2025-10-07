w = input("Membership (y/n) :").lower()
s = float(input("Total amount :"))
discount = 0
if w == 'y':
    if s >= 1000:
        discount = s * 0.20
    elif s >= 500 and s < 1000:
        discount = s * 0.10
elif w == "n":
    if s >= 1000:
        discount = s * 0.05
final_amount = s - discount
print(f"Discount : {discount:.2f}")
print(f"Final Amount to Pay : {final_amount:.2f}")