m = input("Membership (y/n) : ")
t = int(input("Total amount : "))

if t >= 500:
    if t >= 1000 and m == 'y':
        d = t*(20/100)
    elif t < 1000 and m == 'y':
        d = t*(10/100)
    elif t >= 1000 and m == 'n':
        d = t*(5/100)
    else:
        d = 0
else:
    d = 0
print(f"Discount : {d:.2f}")
print(f"Final Amount to Pay : {(t-d):.2f}")