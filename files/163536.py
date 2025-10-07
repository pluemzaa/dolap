Mem = input("Membership (y/n) : ")
to = int(input("Total amount : "))
if Mem == 'y':
    if to >= 500 and to <= 999:
        discount = to*0.1
    elif to >= 1000:
        discount = to*0.2
    else:
        discount = 0.00
else:
    if to >= 1000:
        discount = to*0.05
    else:
        discount = 0.00
pay = to-discount
print("Discount: %.2f" %discount)
print("Final Amount to Pay : %.2f" %pay)