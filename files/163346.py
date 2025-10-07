m = input ("Membership (y/n) : ")
t = int (input("Total amount : "))

if m == 'y':
    if t >= 1000:
        d = t * 0.2
    elif t >= 500 :
        d = t * 0.1 
    else:
        d = 0
elif m == 'n':
    if t >= 1000:
        d = t*0.05
    else:
        d = 0
else:
    d = 0

fp = t-d
print(f"Discount : {d:.2f}")
print(f"Final Amount to Pay : {fp:.2f}")