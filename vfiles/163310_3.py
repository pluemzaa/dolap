m = input("Membership (y/n) :")
t = float(input("Total amount :"))
d = float


if m == "y" :
    if t >= 1000 :
        d = 0.2*t
    elif t >= 500 :
        d = 0.1*t
else :
    if t >= 1000 :
        d = 0.05*t  

f = t-d
print(f"Discount : {d:.2f}")
print(f"Final Amount to Pay : {f:.2f}")