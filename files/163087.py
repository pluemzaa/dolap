m = input("Membership (y/n) : ")
a = int(input("Total amount : "))

if m == 'y':
    if a >= 1000:
        d =a *0.2
    elif a >=500:
        d = a*0.1
    else:
        d=0
elif m == 'n':
    if a >= 1000:
        d =a *0.05
    else:
        d=0
else:
    d =0

fa = a-d
print(f"Discount : {d:.2f}")
print(f"Final Amount to Pay : {fa:.2f}")