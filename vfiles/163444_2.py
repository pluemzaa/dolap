m = input("Membership (y/n) :")
t = float(input("Total amount :"))
d = 0

if m == "y" and t >= 1000:
    d = t * 0.2
elif m == "y" and t >= 500:
    d = t * 0.1
elif m == "n" and t >= 1000:
    d = t * 0.05
    
print(f"Discount : {d:.2f}")
print(f"Final Amount to Pay : {t - d:.2f}")