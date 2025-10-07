M = input("Membership (y/n) :")
P = int(input("Total amount : "))

if M == "y":
    if P >= 1000:
        T = P*(20/100)
        print(f"Discount : {T:.2f}")
    elif 900 >= P >= 500:
        T = P*(10/100)
        print(f"Discount : {T:.2f}")
    else:
        T = 0
        print(f"Discount : {T:.2f}")
elif M == "n":
    if P >= 1000:
        T = P*(5/100)
        print(f"Discount : {T:.2f}")
    else:
        T = 0
        print(f"Discount : {T:.2f}")
TO = P-T
print("Final Amount to Pay :", f"{TO:.2f}")