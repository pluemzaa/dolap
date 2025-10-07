mb = input("Membership (y/n) : ")
item = float(input("Total amount : "))
discount = 0.00
if mb == "y":
    if item >= 1000:
        discount = item * 0.20
    elif item >= 500:
        discount = item * 0.10
    else:
        discount = 0.00
if mb == "n":
    if item >= 1000:
        discount = item * 0.05
    else:
        discount = 0.00
final_amount = item - discount
print(f"Discount : {discount:.2f}")
print(f"Final Amount to Pay : {final_amount:.2f}")