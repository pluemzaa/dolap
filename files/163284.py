jekmember = input("Membership (y/n) : ")
price = int(input("Total amount : "))

if jekmember == ("y"):
    if price >= 1000:
        dis = price*20/100
    elif price >= 500 and price <= 999:
        dis = price*10/100
    else:
        dis=0
else:
    if price >= 1000:
        dis = price*5/100
    else:
        dis =0

print("Discount : ","%.2f"%dis)
final = price - dis 
print("Final Amount to Pay : ""%.2f"%final)