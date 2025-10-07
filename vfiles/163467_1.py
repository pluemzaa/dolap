member = input("Membership (y/n) :")
total = float(input("Total amount :"))
amount = 0

if member =='y':
    discount = total*0.2
    amount = total - discount
    print(f"Discount :{discount:.2f}")
    print(f"Final Amount to Pay :{amount:.2f}")