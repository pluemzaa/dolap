z = (input("Membership (y/n) : "))
x = float(input("Total amount : "))
d = 0

if z == 'y':

    if x >= 1000:
        d = x * 0.2
    elif x >= 500:
        d = x * 0.1
    else:
        r = x
else:
    if x >= 1000:
        d = x * 0.05
print(f"Discount : {d:.2f}")
print(f"Final Amount to Pay : {x - d:.2f}")