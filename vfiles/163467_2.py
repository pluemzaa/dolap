member = input("Membership (y/n) :")
total = float(input("Total amount :"))
amount = 0

if member =='y':
    if total >= 1000:
        discount = total*0.2
        amount = total - discount
        print(f"Discount :{discount:.2f}")
        print(f"Final Amount to Pay :{amount:.2f}")
    elif total = 500 and total < 900:
        discount = total*0.1
        amount = total - discount
        print(f"Discount :{discount:.2f}")
        print(f"Final Amount to Pay :{amount:.2f}")
else:
    if total >= 1000:
        discount = total*0.05
        amount = total - discount
        print(f"Discount :{discount:.2f}")
        print(f"Final Amount to Pay :{amount:.2f}")