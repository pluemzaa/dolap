a = input("Membership (y/n) : ")
b = float(input("Total amount : "))
c = 0

if a == "y":
    if b >= 1000:
        c = 0.2*b
    elif b >= 500:
        c = 0.1*b
else:
    if b >= 1000:
        c = 0.05*b

d = b-c
print(f"Discount : {c:.2f}")
print(f"Final Amount to Pay : {d:.2f}")