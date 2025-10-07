mem = input("Membership (y/n) : ")
to = int(input("Total amount : "))
pay = 0
payy = 0
if mem == "y":
    if to >= 1000:
        dis = 0.20
        pay = to * dis
        payy = to - pay
    elif to >= 500 and to <= 999:
        dis = 0.10
        pay = to * dis
        payy = to - pay
    else:
        dis = 0
        pay = to * dis
        payy = to - pay
else:
    if to >= 1000:
        dis = 0.05
        pay = to * dis
        payy = to - pay
    else:
        dis = 0
        pay = to * dis
        payy = to - pay
print(f"Discount : {pay:.2f}")
print(f"Final Amount to Pay : {payy:.2f}")