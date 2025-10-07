m = input("Membership (y/n) : ")
a = int(input("Total amount : "))

dd = 0

if m == "y" and a >= 1000:
    dd = 0.2
elif m == "y" and a >= 500:
    dd = 0.1
elif m == "n" and a >= 1000:
    dd = 0.05    

if a > 0:
    print(f"Discount : {a * dd:.2f}")
    print(f"Final Amount to Pay : {a * (1 - dd):.2f}")