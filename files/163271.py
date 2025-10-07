x=input("Membership (y/n) : ")

if x=="y":
    tot=float(input("Total amount : "))
    if tot>=1000:
        dis=tot*20/100
        print(f"Discount : {dis:.2f}")
        o=tot-dis
        print(f"Final Amount to Pay : {o:.2f}")
    elif tot>=500:
        dis=tot*10/100
        print(f"Discount : {dis:.2f}")
        o=tot-dis
        print(f"Final Amount to Pay : {o:.2f}")
    else :
        dis=tot*0
        print(f"Discount : {dis:.2f}")
        print(f"Final Amount to Pay : {tot:.2f}")
elif x=="n":
    tot=float(input("Total amount : "))
    if tot >=1000:
        dis=tot*5/100
        print(f"Discount : {dis:.2f}")
        o=tot-dis
        print(f"Final Amount to Pay : {o:.2f}")
    else :
        dis=tot*0/100
        print(f"Discount : {dis:.2f}")
        o=tot-dis
        print(f"Final Amount to Pay : {o:.2f}")