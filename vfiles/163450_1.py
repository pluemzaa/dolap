ji = input("Membership (y/n) : ")
gi = int(input("Total amount : "))

if ji == 'y' and gi >= 1000:
    dis  = gi / 0.2
    total = gi - dis
    print(f"Discount : {dis:.2f}")
    print(f"Final Amount to Pay : {total:.2f}")
    
elif ji == 'y' and 500 <= gi <= 999 :
    dis  = gi / 0.1
    total = gi - dis
    print(f"Discount : {dis:.2f}")
    print(f"Final Amount to Pay : {total:.2f}")

elif ji == 'n' and gi >= 1000 :
    dis  = gi / 0.05
    total = gi - dis
    print(f"Discount : {dis:.2f}")
    print(f"Final Amount to Pay : {total:.2f}")
    
else:
    dis = 0
    total = gi
    print(f"Discount : {dis:.2f}")
    print(f"Final Amount to Pay : {total:.2f}")