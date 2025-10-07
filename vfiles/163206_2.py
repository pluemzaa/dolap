membership = input("Membership (y/n) : ")
amount = int(input("Total amount : "))
discount = 0
if membership == 'y':
    if amount >= 1000:
        discount = amount * 0.2
    elif amount >= 500 and amount <= 999:
        discount = amount * 0.1 
else:
    if amount >= 1000:
        discount = amount * 0.1 

print(f"Discount : {discount:.2f}")
final = amount - discount
print(f"Final Amount to Pay : {final:.2f}")