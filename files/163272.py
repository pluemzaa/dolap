M = input("Membership (y/n) : ")
price = float(input("Total amount : "))



if M == "y":
    if price >= 1000:
        discount = 20
    elif price >= 500:
        discount = 10
    else:
        discount= 0
elif M == "n":
    if price >= 1000:
        discount = 5
    else :
        discount = 0

Dis = (price/100)*discount
total = price-Dis

print (f"Discount : {Dis:.2f}")
print (f"Final Amount to Pay : {total:.2f}")