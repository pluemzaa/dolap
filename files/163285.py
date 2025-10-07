v = input("Membership (y/n) :")
h = int(input("Total amount :"))
fee = 0
if v=='y' :
    if h >= 1000 :
        dis=h*20/100
        print(f"Discount : {dis:.2f}")
    elif h >= 500 and h <= 999 :
        dis=h*10/100
        print(f"Discount : {dis:.2f}")
    else  :
        dis=0
        print(f"Discount : {dis:.2f}")
    print(f'Final Amount to Pay :{h-dis:.2f}')
elif v=='n' :
    if h >= 1000 :
        dis=h*5/100
        print(f"Discount : {dis:.2f}")
    else  :
        dis=0
        print(f"Discount : {dis:.2f}")
    print(f'Final Amount to Pay :{h-dis:.2f}')