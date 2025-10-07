mb = input("Membership (y/n) :")
tt = float(input("Total amount :"))
d = 0

if mb == 'y':
    if tt >= 1000:
        d = tt * 0.20
    elif tt >= 500:
        d = tt * 0.10
else:
    if mb == 'n':
       if tt >= 1000:
           d = tt * 0.05
final = tt - d

print(f"Discount : {d:.2f}")
print(f"Final Amount to Pay : {final:.2f}")