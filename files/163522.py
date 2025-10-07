yesno = input("Membership (y/n) : ")
mem = float(input("Total amount : "))



if yesno == "y":
    if mem >= 1000:
        discount = 20
    elif mem >= 500:
        discount = 10
    else:
        discount= 0
elif yesno == "n":
    if mem >= 1000:
        discount = 5
    else :
        discount = 0

Dis = (mem/100)*discount
total = mem-Dis

print (f"Discount : {Dis:.2f}")
print (f"Final Amount to Pay : {total:.2f}")