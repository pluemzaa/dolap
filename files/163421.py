m = input("Membership (y/n) :")
p = int(input("Total amount : "))

if m == "y":
    if p >= 1000:
        d = p * (20/100)
        total = p - d
        print(f"Discount : {d:.2f}")
        print(f"Final Amount to Pay : {total:.2f}")
    elif p >= 500:
        d = p * (10/100)
        total = p - d
        print(f"Discount : {d:.2f}")
        print(f"Final Amount to Pay : {total:.2f}")
    else:
        d = 0
        print(f"Discount : {d:.2f}")
        print(f"Final Amount to Pay : {p:.2f}")
elif m == "n":
    if p >= 1000:
        d = p * (5/100)
        total = p - d
        print(f"Discount : {d:.2f}")
        print(f"Final Amount to Pay : {total:.2f}")
    else:
        d = 0
        print(f"Discount : {d:.2f}")
        print(f"Final Amount to Pay : {p:.2f}")
else:
    print("เขียนผิดป่าว")