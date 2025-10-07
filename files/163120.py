m = input("Membership (y/n) : ")
b = float(input("Total amount : "))
discount = 0
if m == "y" :
    if b >= 1000:
        discount = b*0.20
    elif b >= 500:
        discount = b*0.10
else:
    if b >= 1000 :
        discount = b*0.05 
final = b - discount
print(f"Discount : {discount:.2f}" )
print(f"Final Amount to Pay : {final:.2f}")