member = input("Membership (y/n) :")
total = int(input("Total amount :"))
discount = 0
if member == "y":
    if total >= 500 and total <= 999:
        discount = total*0.1
    elif total >= 1000:
        discount = total*0.2

elif member == "n":
    if total >=1000:
        discount = total*0.05
s = total - discount
print(f"Discount : {discount:.2f}")
print(f"Final Amount to Pay : {s:.2f}")