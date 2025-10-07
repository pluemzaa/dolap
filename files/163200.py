mem=input("Membership (y/n) : ")
total=int(input("Total amount : "))
dis=0
if mem =="y":
    if total >=1000:
        dis=0.2*total
    elif total>=500:
        dis=0.1*total   
else:
    if total>=1000:
        dis=0.05*total

final=total-dis
print(f"Discount : {dis:.2f}")
print(f"Final Amount to Pay : {final:.2f}")