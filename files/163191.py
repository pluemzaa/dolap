mb = input("Membership (y/n) :")
ta = float(input("Total amount :"))
discount = 0

if mb == "y":
    if ta >=1000:
        discount = ta * 0.2
    elif ta >=500:
        discount = ta * 0.1
else:
    if ta >=1000:
        discount = ta * 0.05
fa = ta - discount   
print(f"discount :{discount:.2f}")
print(f"Final Amount to Pay :{fa:.2f}")