mem = input("Membership (y/n) : ") 
ta = float(input("Total amount : "))
discount = 0
if mem == 'y': 
    if ta >= 1000:
        discount = ta * 0.20 
    elif ta >= 500: 
        discount = ta * 0.10 
else: 
     if ta >= 1000: 
         discount = ta * 0.05

final = ta - discount

print(f"Discount : {discount:.2f} ")
print(f"Final Amount to Pay : {final:.2f} ")