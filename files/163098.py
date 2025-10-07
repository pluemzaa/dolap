mem = input("Membership (y/n) : ")
coast = float(input("Total amount : "))
dis = 0
if mem == "y" :
    if coast >= 1000 :
        dis = coast * 0.20
    elif coast >= 500 :
        dis = coast * 0.10
else :
    if coast >= 1000 :
        dis = coast * 0.05
tt = coast - dis

print(f"Discount : {dis:.2f} ")
print(f'Final Amount to Pay : {tt:.2f} ')