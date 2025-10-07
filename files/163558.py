Member = input("Membership (y/n) :")
total = int(input("Total amount :"))
if Member == 'y':
    if total >= 1000:
        D =  total*0.2
    elif total >= 500 and total <= 999:
        D = total*0.1
    else:
        D = 0.00
else:
    if total >= 1000:
        D = total*0.05
    else:
        D = 0.00

P = total-D
print(f"Discount : {D:.2f}")
print(f"Final Amount to Pay : {P:.2f}")