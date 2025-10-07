mem = input("Membership (y/n) : ")
amout = float(input('Total amount : '))
if mem == "y":
    if amout >= 1000:
        discout = (amout*20)/100
    elif amout >= 500 and amout <= 999 :
        discout = (amout*10)/100
    else:
        discout = 0
else :
    if amout >= 1000:
        discout = (amout*5)/100
    else:
        discout = 0
total = amout - discout
print(f"Discount : {discout:.2f}")
print(f"Final Amount to Pay : {total:.2f}")